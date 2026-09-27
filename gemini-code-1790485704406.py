import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "JDsMR1bHGO4"
url = f"https://www.youtube.com/watch?v={video_id}"

# 1. Traditional Scraping for Metadata (Title)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find("meta", itemprop="name")["content"]
print(f"Scraped Title: {title}\n")

# 2. Extracting the Subtitle Data
try:
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)
    print("Transcript successfully scraped. Sample lines:")
    for entry in transcript[:5]:
        print(f"[{entry.start:.2f}] {entry.text}")
except Exception as e:
    print(f"Could not scrape transcript: {e}")