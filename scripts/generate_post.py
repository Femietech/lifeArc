import os
import json
import random
import datetime
from openai import OpenAI

# Load topics
with open("topics.json", "r") as f:
    data = json.load(f)
topics = data["topics"]

# Pick a topic (simple round-robin by day of year to avoid repeats)
day_of_year = datetime.datetime.now().timetuple().tm_yday
topic_index = day_of_year % len(topics)
topic = topics[topic_index]

# Generate content using OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = f"Write a detailed, educational blog post about '{topic}' for a finance blog. Include practical advice and examples. Keep it around 500 words."
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=800
)
content = response.choices[0].message.content

# Create post filename with date
today = datetime.date.today()
filename = f"_posts/{today.strftime('%Y-%m-%d')}-{topic.lower().replace(' ', '-')}.md"

# Jekyll front matter
post_content = f"""---
title: "{topic}"
date: {today}
categories: [finance]
---

{content}
"""

# Write file
with open(filename, "w") as f:
    f.write(post_content)

print(f"Generated post: {filename}")
