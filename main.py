import requests

api_key = "086db17afc0b4c3280600bfe1934e0da"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-25&sortBy=publishedAt&" \
      "apiKey=" + api_key

request = requests.get(url)
content = request.text
print(content)