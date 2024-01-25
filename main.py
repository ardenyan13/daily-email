import requests
from send_email import send_email

topic = "tesla"
api_key = "086db17afc0b4c3280600bfe1934e0da"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=086db17afc0b4c3280600bfe1934e0da&"
       "language=en")

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# get the article titles and description
message = "Subject: Today's news \n"
for article in content["articles"][:20]:
    # some articles may have null titles or null descriptions
    if article["title"] and article["description"]:
        message += (article["title"] + "\n" + article["description"] + "\n"
                    + article["url"] + "\n\n")

message = message.encode("utf-8")
send_email(message)
