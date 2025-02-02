"""Configuration settings for the agents module."""
import os

# OpenAI API configuration
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

# Set environment variable for LoopGPT
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
