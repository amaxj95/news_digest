import requests

API_KEY = "1cc408d3e5c5427982ffed3df4418df7"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-02-24&sortBy=publishedAt&apiKey=" \
      "1cc408d3e5c5427982ffed3df4418df7"

# Make Request
request = requests.get(url)

#Get data dictionary
content = request.json()

# Access article titles
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
