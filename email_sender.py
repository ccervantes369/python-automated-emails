# Api Key: 
import requests

class NewsFeed:
    def __init__(self, data):
        self.data = data

    def get(self):
        pass

response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2025-06-13&sortBy=publishedAt&apiKey=c0535a314cf84b7fac8469d6ad277d79")
content = response.text
print(content)