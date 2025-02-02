"""Test script for Redis pub/sub communication"""
import asyncio
import redis.asyncio as redis
import json
from datetime import datetime
import uuid

async def main():
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0)
    
    try:
        print("🔌 Connected to Redis")
        
        # Clear any existing messages
        try:
            await r.delete('agent:loopgpt:inbox')
            await r.delete('agent:windsurf:inbox')
            print("🧹 Cleared existing messages")
        except Exception as e:
            print(f"⚠️ Error clearing messages: {e}")
        
        # Test message
        message = {
            'id': str(uuid.uuid4()),
            'timestamp': datetime.utcnow().isoformat(),
            'sender': 'windsurf',
            'content': {
                'query': 'Analyze current soccer events',
                'context': {
                    'sport': 'SOCCER',
                    'analysis_type': 'live_events'
                }
            }
        }
        
        print(f"\n📤 Sending test message: {json.dumps(message, indent=2)}")
        
        # Send message to LoopGPT's inbox
        msg_id = await r.xadd(
            'agent:loopgpt:inbox',
            fields={
                'id': message['id'],
                'timestamp': message['timestamp'],
                'sender': message['sender'],
                'content': json.dumps(message['content'])
            }
        )
        print(f"✅ Message sent with ID: {msg_id}")
        
        # Wait for and print responses
        print("\n👂 Listening for responses...")
        
        # Create a new consumer group if it doesn't exist
        try:
            await r.xgroup_create('agent:windsurf:inbox', 'test_group', mkstream=True)
            print("✨ Created new consumer group: test_group")
        except redis.ResponseError:
            print("ℹ️ Consumer group already exists")
        
        # Listen for responses for 10 seconds
        start_time = datetime.utcnow()
        while (datetime.utcnow() - start_time).total_seconds() < 10:
            # Read new messages
            try:
                messages = await r.xreadgroup(
                    'test_group',
                    'test_consumer',
                    {'agent:windsurf:inbox': '>'},
                    count=1,
                    block=1000
                )
                
                for stream, stream_messages in messages:
                    for msg_id, msg_data in stream_messages:
                        print(f"\n📨 Received response:")
                        print(f"Message ID: {msg_id}")
                        
                        # Parse and format response
                        try:
                            content = json.loads(msg_data[b'content'].decode())
                            print("Content:", json.dumps(content, indent=2))
                        except Exception as e:
                            print(f"Raw data: {msg_data}")
                        
                        # Acknowledge message
                        await r.xack('agent:windsurf:inbox', 'test_group', msg_id)
                        print("✅ Message acknowledged")
                        
            except Exception as e:
                print(f"❌ Error reading messages: {e}")
                continue
        
        print("\n⏱️ Test complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Clean up
        await r.close()
        print("🔌 Disconnected from Redis")

if __name__ == "__main__":
    asyncio.run(main())
