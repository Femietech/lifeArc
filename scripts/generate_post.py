import os
import json
import random
from google import genai

# Load topics
try:
    with open("topics.json", "r") as f:
        data = json.load(f)
    topic = random.choice(data["topics"])
except Exception as e:
    print(f"Error loading topics: {e}")
    topic = "Digital Design Trends in 2026"

# Configure Gemini Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Generate Content
prompt = f"Write a professional, engaging blog post about {topic} for a finance and tech blog. Include a catchy title."
response = client.models.generate_content(
    model="gemini-2.0-flash", # Using the latest 2026 standard model
    contents=prompt
)

print(f"Generated Post: {response.text}")
# Note: Add your Blogger posting code below if it was in your previous version
