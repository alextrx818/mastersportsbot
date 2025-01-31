from core.logging_config import setup_debug_mode
from core.debug import DEBUG_MODE, debug_trace
import asyncio

@debug_trace
async def test_function():
    print("Testing logging system")
    raise Exception("Test error message")

async def main():
    # Setup logging in debug mode
    setup_debug_mode()
    DEBUG_MODE.enable()
    
    try:
        await test_function()
    except Exception as e:
        print(f"Caught error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
