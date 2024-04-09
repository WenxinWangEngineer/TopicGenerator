import requests
# import json


def fetch_news(topics, api_key):
    articles = []
    for topic in topics:
        url = f"https://gnews.io/api/v4/search?q={topic}&token={api_key}"
        response = requests.get(url)
        data = response.json()
        articles.extend(data['articles'])
    return articles
