from os import environ
from newsapi import NewsApiClient

query = "tesla"
# Init
newsapi = NewsApiClient(api_key=environ["NEWSAPIKEY"])

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q=query, country="us", language="en", category="business")
# /v2/sources
sources = newsapi.get_sources()
outputs = []

for x in top_headlines["articles"]:
    output = {}
    output["title"] = x["title"]
    output["url"] = x["url"]
    outputs.append(output)

print(outputs)
