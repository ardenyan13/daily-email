import requests
from send_email import send_email

api_key = "086db17afc0b4c3280600bfe1934e0da"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-25&sortBy=publishedAt&" \
      "apiKey=086db17afc0b4c3280600bfe1934e0da"

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# get the article titles and description
message = ""
for article in content["articles"]:
    # some articles may have null titles or null descriptions
    if article["title"] and article["description"]:
        message = message + article["title"] + "\n" + article["description"] + "\n\n"

message = message.encode("utf-8")
send_email(message)
