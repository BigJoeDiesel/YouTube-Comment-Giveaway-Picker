# ytcmt_picker.py
# Appends winner to ytcmtwinners.txt in the same folder

import random
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

# ────────────────────────────────────────
API_KEY = "YOUR API KEY HERE"  # <- your api key from google.
VIDEO_INPUT = "YOUR VIDEO LINK HERE"  # ← your link/ID.
MAX_COMMENTS = 200  # <- change number to the amount of comments you want to pick from.
LOG_FILE = "ytcmtwinners.txt"  # ← changed to your requested name.
# ────────────DEV─────BigJoeDiesel─&─Xai──────

def extract_video_id(url_or_id):
    if len(url_or_id) == 11 and re.match(r'^[A-Za-z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'youtu\.be\/([0-9A-Za-z_-]{11})',
        r'^([0-9A-Za-z_-]{11})$'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    
    raise ValueError("Could not extract valid video ID.")

try:
    VIDEO_ID = extract_video_id(VIDEO_INPUT)
    print(f"Video ID: {VIDEO_ID}\n")
except ValueError as e:
    print(e)
    exit(1)

youtube = build("youtube", "v3", developerKey=API_KEY)

print("Fetching comments...\n")

comments = []
next_page = ""

try:
    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=VIDEO_ID,
            maxResults=100,
            pageToken=next_page if next_page else None
        )
        response = request.execute()

        for item in response.get("items", []):
            author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            if author not in comments:
                comments.append(author)

        next_page = response.get("nextPageToken")
        if not next_page or len(comments) >= MAX_COMMENTS:
            break

    if not comments:
        print("No comments found.")
    else:
        winner = random.choice(comments)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Found {len(comments)} unique commenters.")
        print(f"Winner: 🎉 {winner} 🎉")
        
        # Append to file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} | Video: {VIDEO_ID} | Winner: {winner}\n")
        
        print(f"Saved to: {LOG_FILE} (appended, old winners preserved)")

except Exception as e:
    print("Error:", e)