"""Test script for agent bridge communication"""
from agent_bridge import AgentBridge
import asyncio
import sys
import os

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)

async def test():
    bridge = AgentBridge()
    await bridge.connect()  # Ensure connection is established
    
    print("Connected to Redis")
    
    # Send message and wait for response
    print("Sending message to LoopGPT...")
    message = {
        'query': 'Analyze current soccer events',
        'context': {'sport': 'SOCCER'}
    }
    print(f"Message: {message}")
    
    try:
        response = await bridge.send_to_loopgpt(message)
        print('Response:', response)
    except Exception as e:
        print(f"Error sending message: {e}")
    
    # Wait a bit to ensure message is processed
    print("Waiting for message processing...")
    await asyncio.sleep(5)
    
    # Check analysis results
    if response and response.get('analysis_id'):
        analysis = await bridge.get_analysis(response['analysis_id'])
        print('\nAnalysis:', analysis)
    else:
        print("No analysis ID received")
    
    await bridge.close()

if __name__ == "__main__":
    asyncio.run(test())
