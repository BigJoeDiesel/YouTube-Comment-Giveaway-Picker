# YouTube Comment Giveaway Picker

A simple, free Python script that fetches comments from **one of your own YouTube videos**, picks a random commenter, and logs the winner to a text file. Perfect for giveaways, fan shoutouts, or engagement contests — no paid tools required.

Built with the YouTube Data API v3 + a bit of help from Grok (xAI).  
Created by: BigJoeDiesel™

## Features
- Accepts full YouTube URL or plain video ID
- Fetches up to 200 unique top-level commenters (adjustable)
- Picks one random winner instantly
- Automatically appends winner + timestamp + video ID to `ytcmtwinners.txt`
- Handles common errors with helpful messages
- No GUI, no dependencies beyond the Google API client

## Requirements
- Python 3.8+
- A free YouTube Data API v3 key (takes ~2 minutes to get)

## Installation

1. **Get your API Key** (required – only once)
   - Go to: https://console.cloud.google.com/apis/library/youtube.googleapis.com
   - Enable the "YouTube Data API v3"
   - Go to Credentials → Create Credentials → API Key
   - Copy the key (looks like `AIzaSyC...`)

2. **Install the one required package**  
   Open Command Prompt / Terminal and run:


3. **Download the script**
- Save the code below as `ytcmt_picker.py` (or clone this repo)

## Usage

1. Edit the script (top section):
```python
API_KEY = "paste-your-api-key-here"
VIDEO_INPUT = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"  # or just the ID

Run IT:
python ytcmt_picker.py

Output example:
Video ID: l2xdYACyMSU

Fetching comments...

Found 142 unique commenters.
Winner: 🎉 AwesomeFan456 🎉

Saved to: ytcmtwinners.txt (appended, old winners preserved)

→ A new line is added to ytcmtwinners.txt every run:

Example:  2026-02-06 16:45:12 | Video: l2xdYACyMSU | Winner: AwesomeFan456

Important NotesOnly works on videos YOU own (YouTube API restriction for privacy)
Video must be public or unlisted (private videos won't work)
Comments must be enabled on the video
Daily API quota is high (~10,000 units/day) — one run uses very little

Customization IdeasChange MAX_COMMENTS to fetch more/less
Add import pyperclip; pyperclip.copy(winner) to auto-copy winner to clipboard (install pip install pyperclip)
Pick top 3: winners = random.sample(comments, min(3, len(comments)))
Filter usernames: skip bots/spam with a blocklist


