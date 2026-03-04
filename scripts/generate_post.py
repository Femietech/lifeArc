import os
import json
import datetime
import google.generativeai as genai

# Load topics
with open("topics.json", "r") as f:
    data = json.load(f)
topics = data["topics"]

# Pick a topic (round-robin by day of year to avoid repeats)
day_of_year = datetime.datetime.now().timetuple().tm_yday
topic_index = day_of_year % len(topic` s)
topic = topics[topic_index]

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Use the free model (Gemini 1.5 Flash is fast and free)
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = f"Write a detailed, educational blog post about '{topic}' for a finance blog. Include practical advice and examples. Keep it around 500 words. Use markdown formatting."

response = model.generate_content(prompt)
content = response.text

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
