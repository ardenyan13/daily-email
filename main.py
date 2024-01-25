import requests

api_key = "086db17afc0b4c3280600bfe1934e0da"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-25&sortBy=publishedAt&" \
      "apiKey=" + api_key

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# get the article titles and description
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
