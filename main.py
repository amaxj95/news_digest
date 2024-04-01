import requests
from send_email import send_email

API_KEY = "1cc408d3e5c5427982ffed3df4418df7"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=1cc408d3e5c5427982ffed3df4418df7"

# Make request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

# Access the article titles and description
body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    title = article.get("title", "")
    description = article.get("description", "")
    url = article.get("url", "")
    if title:
        body += f"{title}\n{description}\n{url}\n\n"

# Encode the body as UTF-8
body = body.encode("utf-8")

# Send email
send_email(message=body)
