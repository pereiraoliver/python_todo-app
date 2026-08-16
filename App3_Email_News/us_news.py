import os
import smtplib
from email.mime.text import MIMEText

import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GMAIL = os.getenv("GMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
US_DOMAINS = os.getenv("US_DOMAINS")

# Get news
url = "https://newsapi.org/v2/everything"
params = {
    "domains": US_DOMAINS,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 20,
    "apiKey": NEWS_API_KEY,
}

request = requests.get(url, params=params)

data = request.json()

# Build email
body = "<h2>Oliver's US Conservative News</h2>"

for i, article in enumerate(data["articles"], 1):
    body += f"""
    <p>{i}. {article["title"]} (<a href="{article["url"]}">{article["source"]["name"]}</a>)</p>
    """
# Send email
email = MIMEText(body, "html")
email["Subject"] = "Oliver's US Conservative News"
email["From"] = GMAIL
email["To"] = GMAIL

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(GMAIL, GMAIL_APP_PASSWORD)
    server.send_message(email)

print("Email sent!")
