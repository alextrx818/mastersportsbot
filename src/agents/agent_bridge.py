"""Bridge for agent communication using Redis Streams"""
import redis.asyncio as redis
import json
import asyncio
from typing import Dict, Any, Callable, Awaitable
import datetime

class AgentBridge:
    def __init__(self):
        """Initialize the bridge"""
        self.redis = None
        self.streams = {
            'loopgpt_to_windsurf': 'agent:windsurf:inbox',
            'windsurf_to_loopgpt': 'agent:loopgpt:inbox',
            'analysis': 'agent:analysis:results'
        }
        self.handlers = {}
    
    async def connect(self):
        """Connect to Redis and ensure streams exist"""
        print("Connecting to Redis...")
        self.redis = await redis.Redis(host='localhost', port=6379, db=0)
        
        print("Ensuring streams exist...")
        # Create streams and consumer groups if they don't exist
        for stream in self.streams.values():
            try:
                await self.redis.xgroup_create(stream, 'loopgpt_consumers', mkstream=True)
                print(f"✨ Created consumer group for {stream}")
            except redis.ResponseError as e:
                if "BUSYGROUP" in str(e):
                    print(f"ℹ️ Consumer group already exists for {stream}")
                else:
                    print(f"⚠️ Error creating consumer group for {stream}: {e}")
    
    async def close(self):
        """Close Redis connection"""
        if self.redis:
            await self.redis.close()
            self.redis = None
    
    def register_handler(self, stream_name: str, handler: Callable[[Dict[str, Any]], Awaitable[None]]):
        """Register a handler for a stream"""
        print(f"🔗 Registering handler for stream {stream_name}")
        self.handlers[stream_name] = handler
    
    async def start_listening(self):
        """Start listening for messages on all registered streams"""
        print("Starting to listen on streams:", list(self.handlers.keys()))
        
        # Create consumer groups for each stream
        for stream in self.handlers.keys():
            try:
                await self.redis.xgroup_create(stream, 'loopgpt_consumers', mkstream=True)
                print(f"✨ Created consumer group for {stream}")
            except redis.ResponseError as e:
                if "BUSYGROUP" in str(e):
                    print(f"ℹ️ Consumer group already exists for {stream}")
                else:
                    print(f"⚠️ Error creating consumer group for {stream}: {e}")
        
        # Build stream dict for xreadgroup
        streams = {}
        for stream in self.handlers.keys():
            # Ensure stream exists
            try:
                await self.redis.xinfo_groups(stream)
            except redis.ResponseError:
                # Create stream if it doesn't exist
                await self.redis.xadd(stream, {'dummy': 'init'})
                await self.redis.xgroup_create(stream, 'loopgpt_consumers', mkstream=True)
            streams[stream] = '>'
        
        while True:
            try:
                # Read new messages from all streams
                messages = await self.redis.xreadgroup(
                    'loopgpt_consumers',
                    'loopgpt_consumer_1',
                    streams,
                    count=1,
                    block=1000
                )
                
                # Process each message
                for stream_name, stream_messages in messages:
                    stream = stream_name.decode('utf-8')
                    
                    for msg_id, msg_data in stream_messages:
                        print(f"\n📨 Processing message from {stream}:")
                        print(f"Message ID: {msg_id}")
                        
                        # Convert message data to dict
                        msg = {}
                        for key, value in msg_data.items():
                            try:
                                msg[key.decode('utf-8')] = value.decode('utf-8')
                            except Exception as e:
                                print(f"⚠️ Error decoding message field {key}: {e}")
                                continue
                        
                        # Get handler for this stream
                        handler = self.handlers.get(stream)
                        if handler:
                            try:
                                # Parse content if it's JSON
                                if 'content' in msg and isinstance(msg['content'], str):
                                    try:
                                        msg['content'] = json.loads(msg['content'])
                                    except json.JSONDecodeError:
                                        pass  # Keep content as string if not JSON
                                
                                # Call handler
                                await handler(msg)
                                
                                # Acknowledge message
                                await self.redis.xack(stream, 'loopgpt_consumers', msg_id)
                                print(f"✅ Message {msg_id} acknowledged")
                                
                            except Exception as e:
                                print(f"❌ Error in handler for {stream}: {e}")
                        else:
                            print(f"❌ No handler found for {stream}")
                            print(f"🔍 Available handlers: {list(self.handlers.keys())}")
                
            except redis.ResponseError as e:
                print(f"❌ Redis error: {e}")
                await asyncio.sleep(1)  # Wait before retrying
                
            except Exception as e:
                print(f"❌ Error in message loop: {e}")
                await asyncio.sleep(1)  # Wait before retrying
    
    async def publish_analysis(self, analysis: Dict[str, Any]) -> str:
        """Publish analysis results to stream"""
        try:
            # Add timestamp and convert to JSON
            message = {
                'timestamp': datetime.utcnow().isoformat(),
                'analysis': analysis
            }
            
            # Publish to stream
            msg_id = await self.redis.xadd(
                self.streams['analysis'],
                fields={
                    'content': json.dumps(message)
                }
            )
            
            return msg_id.decode('utf-8')
            
        except Exception as e:
            print(f"Error publishing analysis: {e}")
            return None
"""Bridge for communication between Windsurf and LoopGPT agents using Redis Streams"""
import redis.asyncio as redis
import json
import asyncio
from typing import Optional, Dict, Any, Callable
from datetime import datetime, timedelta
import uuid

class AgentBridge:
    """Bridge for inter-agent communication using Redis Streams"""
    
    def __init__(self):
        self.redis = None  # Will be initialized in connect()
        self.streams = {
            'windsurf_to_loopgpt': 'agent:loopgpt:inbox',  # Changed from outbox to inbox
            'loopgpt_to_windsurf': 'agent:windsurf:inbox',  # Changed from outbox to inbox
            'analysis_results': 'agent:analysis:results'
        }
        self.consumer_groups = {
            'windsurf': 'windsurf_consumers',
            'loopgpt': 'loopgpt_consumers'
        }
        self.handlers = {}
    
    async def connect(self):
        """Connect to Redis and ensure streams exist"""
        print("Connecting to Redis...")
        self.redis = await redis.Redis(host='localhost', port=6379, db=0)
        
        print("Ensuring streams exist...")
        # Create streams and consumer groups if they don't exist
        for stream in self.streams.values():
            try:
                await self.redis.xgroup_create(stream, 'loopgpt_consumers', mkstream=True)
                print(f"✨ Created consumer group for {stream}")
            except redis.ResponseError as e:
                if "BUSYGROUP" in str(e):
                    print(f"ℹ️ Consumer group already exists for {stream}")
                else:
                    print(f"⚠️ Error creating consumer group for {stream}: {e}")
    
    async def _ensure_streams_exist(self):
        """Ensure all streams and consumer groups exist"""
        print("Ensuring streams exist...")
        for stream in self.streams.values():
            try:
                # Create stream if it doesn't exist
                await self.redis.xgroup_create(stream, self.consumer_groups['windsurf'], mkstream=True)
                print(f"Created/verified stream {stream} with group {self.consumer_groups['windsurf']}")
            except redis.ResponseError as e:
                if 'BUSYGROUP' not in str(e):  # Ignore if group already exists
                    print(f"Error creating stream {stream}: {e}")
                    raise
            
            try:
                await self.redis.xgroup_create(stream, self.consumer_groups['loopgpt'], mkstream=True)
                print(f"Created/verified stream {stream} with group {self.consumer_groups['loopgpt']}")
            except redis.ResponseError as e:
                if 'BUSYGROUP' not in str(e):
                    print(f"Error creating stream {stream}: {e}")
                    raise
    
    async def send_to_loopgpt(self, message: Dict[str, Any], timeout: int = 30) -> Optional[Dict[str, Any]]:
        """Send a message to LoopGPT and wait for response"""
        await self.connect()
        
        message_id = str(uuid.uuid4())
        message_data = {
            'id': message_id,
            'timestamp': datetime.utcnow().isoformat(),
            'sender': 'windsurf',
            'content': json.dumps(message)
        }
        
        print(f"Sending message to LoopGPT stream: {message_data}")
        
        # Add message to stream
        await self.redis.xadd(
            self.streams['windsurf_to_loopgpt'],
            fields=message_data
        )
        
        print("Message sent, waiting for response...")
        
        # Wait for response
        start_time = asyncio.get_event_loop().time()
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            # Read from response stream
            response = await self.redis.xread(
                {self.streams['loopgpt_to_windsurf']: 0},
                count=1,
                block=1000
            )
            
            if response:
                stream_name, messages = response[0]
                for msg_id, msg_data in messages:
                    if msg_data[b'id'].decode() == message_id:
                        # Acknowledge message
                        await self.redis.xack(
                            stream_name,
                            self.consumer_groups['windsurf'],
                            msg_id
                        )
                        content = json.loads(msg_data[b'content'].decode())
                        print(f"Received response: {content}")
                        return content
            
            await asyncio.sleep(0.1)
        
        print("Timeout waiting for response")
        return None
    
    async def send_to_windsurf(self, message: Dict[str, Any], timeout: int = 30) -> Optional[Dict[str, Any]]:
        """Send a message to Windsurf and wait for response"""
        await self.connect()
        
        message_id = str(uuid.uuid4())
        message_data = {
            'id': message_id,
            'timestamp': datetime.utcnow().isoformat(),
            'sender': 'loopgpt',
            'content': json.dumps(message)
        }
        
        print(f"Sending message to Windsurf stream: {message_data}")
        
        # Add message to stream
        await self.redis.xadd(
            self.streams['loopgpt_to_windsurf'],
            fields=message_data
        )
        
        print("Message sent, waiting for response...")
        
        # Wait for response
        start_time = asyncio.get_event_loop().time()
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            # Read from response stream
            response = await self.redis.xread(
                {self.streams['windsurf_to_loopgpt']: 0},
                count=1,
                block=1000
            )
            
            if response:
                stream_name, messages = response[0]
                for msg_id, msg_data in messages:
                    if msg_data[b'id'].decode() == message_id:
                        # Acknowledge message
                        await self.redis.xack(
                            stream_name,
                            self.consumer_groups['loopgpt'],
                            msg_id
                        )
                        content = json.loads(msg_data[b'content'].decode())
                        print(f"Received response: {content}")
                        return content
            
            await asyncio.sleep(0.1)
        
        print("Timeout waiting for response")
        return None
    
    def register_handler(self, stream: str, handler: Callable[[Dict[str, Any]], None]):
        """Register a message handler for a stream"""
        print(f"🔗 Registering handler for stream {stream}")
        # Store both string and bytes versions of the stream name
        self.handlers[stream] = handler
        self.handlers[stream.encode()] = handler
    
    async def start_listening(self):
        """Start listening for messages on all streams"""
        await self.connect()
        
        # Get last message IDs
        last_ids = {stream: '0-0' for stream in self.streams.values()}
        print(f"Starting to listen on streams: {list(self.streams.values())}")
        
        while True:
            try:
                # Read new messages from each stream
                for stream, name in self.streams.items():
                    # Read pending messages first
                    pending = await self.redis.xpending(
                        name,
                        self.consumer_groups['loopgpt']
                    )
                    
                    if pending and pending['pending']:
                        print(f"Found {pending['pending']} pending messages in {name}")
                        # Process pending messages
                        messages = await self.redis.xrange(
                            name,
                            min=pending['min'],
                            max=pending['max']
                        )
                        for msg_id, msg_data in messages:
                            await self._process_message(name, msg_id, msg_data)
                    
                    # Read new messages
                    response = await self.redis.xread(
                        {name: last_ids[name]},
                        count=10,
                        block=1000
                    )
                    
                    if response:
                        print(f"Received new messages in {name}")
                        for stream_name, messages in response:
                            for msg_id, msg_data in messages:
                                await self._process_message(stream_name, msg_id, msg_data)
                                last_ids[stream_name.decode()] = msg_id.decode()
                
                await asyncio.sleep(0.1)  # Prevent busy waiting
            except Exception as e:
                print(f"Error in message loop: {e}")
                await asyncio.sleep(1)  # Back off on error
    
    async def _process_message(self, stream: bytes, msg_id: bytes, msg_data: Dict[bytes, bytes]):
        """Process a single message"""
        try:
            print(f"\nProcessing message from {stream}:")
            print(f"Message ID: {msg_id}")
            print(f"Raw data: {msg_data}")
            
            # Convert message data
            try:
                message = {
                    'id': msg_data[b'id'].decode(),
                    'timestamp': msg_data[b'timestamp'].decode(),
                    'sender': msg_data[b'sender'].decode()
                }
                
                # Handle content specially since it might be JSON
                content = msg_data[b'content'].decode()
                try:
                    message['content'] = json.loads(content)
                except json.JSONDecodeError:
                    print(f"⚠️ Content is not JSON: {content}")
                    message['content'] = content
                
                print(f"📨 Processed message: {message}")
                
                # Handle message if handler exists
                handler = self.handlers.get(stream)
                if handler:
                    print(f"✅ Found handler for {stream}, executing...")
                    await handler(message)
                else:
                    print(f"❌ No handler found for {stream}")
                    print(f"🔍 Available handlers: {list(self.handlers.keys())}")
            
            except KeyError as e:
                print(f"❌ Missing required field in message: {e}")
                print(f"🔍 Available fields: {list(msg_data.keys())}")
            
            # Always acknowledge message to prevent reprocessing
            await self.redis.xack(
                stream,
                self.consumer_groups['loopgpt'],
                msg_id
            )
            print("✅ Message acknowledged")
            
        except Exception as e:
            print(f"❌ Error processing message {msg_id}: {e}")
            # Still acknowledge to prevent endless retries
            try:
                await self.redis.xack(
                    stream,
                    self.consumer_groups['loopgpt'],
                    msg_id
                )
                print("✅ Message acknowledged despite error")
            except Exception as e2:
                print(f"❌ Error acknowledging message: {e2}")
    
    async def publish_analysis(self, analysis: Dict[str, Any]) -> str:
        """Publish analysis results to stream"""
        await self.connect()
        
        analysis_id = str(uuid.uuid4())
        message_data = {
            'id': analysis_id,
            'timestamp': datetime.utcnow().isoformat(),
            'content': json.dumps(analysis)
        }
        
        print(f"Publishing analysis {analysis_id}")
        
        # Add to analysis stream
        await self.redis.xadd(
            self.streams['analysis_results'],
            fields=message_data
        )
        
        return analysis_id
    
    async def get_analysis(self, analysis_id: str, max_age: int = 3600) -> Optional[Dict[str, Any]]:
        """Get analysis results by ID within max age (seconds)"""
        await self.connect()
        
        # Calculate time range
        min_time = (datetime.utcnow() - timedelta(seconds=max_age)).isoformat()
        
        print(f"Looking for analysis {analysis_id}")
        
        # Read from stream
        messages = await self.redis.xrevrange(
            self.streams['analysis_results'],
            count=100  # Limit search
        )
        
        for msg_id, msg_data in messages:
            if msg_data[b'id'].decode() == analysis_id:
                timestamp = msg_data[b'timestamp'].decode()
                if timestamp >= min_time:
                    content = json.loads(msg_data[b'content'].decode())
                    print(f"Found analysis: {content}")
                    return content
        
        print("Analysis not found")
        return None
    
    async def close(self):
        """Close Redis connection"""
        if self.redis:
            print("Closing Redis connection")
            await self.redis.close()
