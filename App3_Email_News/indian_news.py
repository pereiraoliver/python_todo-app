import os
import smtplib

import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GMAIL = os.getenv("GMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
INDIAN_DOMAINS = os.getenv("INDIAN_DOMAINS")

# Get news
url = "https://newsapi.org/v2/everything"

params = {
    "domains": INDIAN_DOMAINS,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 20,
    "apiKey": NEWS_API_KEY,
}

request = requests.get(url, params=params)
data = request.json()

# Build email
body = "<h2>Oliver's India News</h2>"

for i, article in enumerate(data["articles"], 1):
    body += f"""
    <p>
        {i}. {article["title"]} 
        (<a href="{article["url"]}">{article["source"]["name"]}</a>)
    </p>
    """

# Build email manually
email = f"""From: {GMAIL}
To: {GMAIL}
Subject: Oliver's India News
Content-Type: text/html; charset="UTF-8"

{body}
"""

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(GMAIL, GMAIL_APP_PASSWORD)
    server.sendmail(GMAIL, GMAIL, email.encode("utf-8"))

print("Email sent!")
