import os
import json
import random
from google import genai
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# 1. Load Topics
try:
    with open("topics.json", "r") as f:
        data = json.load(f)
    topic = random.choice(data["topics"])
except Exception as e:
    print(f"Error loading topics: {e}")
    topic = "The Future of Digital Architecture and Finance"

# 2. Generate Content with Gemini 2.0
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
prompt = f"Write a professional blog post about {topic}. Include a Title at the top and use HTML <h3> tags for subheadings. Keep it engaging for tech enthusiasts."

print(f"Generating post for topic: {topic}...")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)
full_text = response.text

# Split the first line as Title, the rest as Body
lines = full_text.split('\n')
title = lines[0].replace('#', '').strip()
body = '\n'.join(lines[1:]).replace('\n', '<br>')

# 3. Setup Blogger Connection
creds = Credentials(
    None,
    refresh_token=os.environ["BLOGGER_REFRESH_TOKEN"],
    client_id=os.environ["BLOGGER_CLIENT_ID"],
    client_secret=os.environ["BLOGGER_CLIENT_SECRET"],
    token_uri="https://oauth2.googleapis.com/token",
)
service = build("blogger", "v3", credentials=creds)

# 4. Post to Blogger
blog_id = os.environ["BLOGGER_BLOG_ID"]
new_post = {
    "kind": "blogger#post",
    "blog": {"id": blog_id},
    "title": title,
    "content": body
}

print(f"Attempting to post to Blog ID: {blog_id}...")
posts = service.posts().insert(blogId=blog_id, body=new_post).execute()

print(f"SUCCESS! Post published at: {posts.get('url')}")
