from redis_client import RedisClient

# Initialize the Redis client
redis_client = RedisClient()

# Define the channel for communication
channel = 'loopgpt_channel'

# Publish a test message
redis_client.publish(channel, 'Hello LoopGPT!')

# Subscribe and listen for messages
pubsub = redis_client.subscribe(channel)
print("Listening for messages...")
for message in redis_client.listen(pubsub):
    print(f"Received message: {message}")
    break  # Exit after receiving the first message to complete the test
