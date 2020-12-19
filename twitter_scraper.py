import twint
import json
import re

query = "tesla"

config = twint.Config()
config.Search = query
config.Limit = 500
config.Store_json = True
config.Output = "output.json"

twint.run.Search(config)


def clean_tweet(tweet):
    tweet = re.sub("#\w*", "", tweet)  # remove hashtags
    tweet = re.sub("@\w*", "", tweet)  # remove @
    tweet = re.sub("&amp", "", tweet)
    tweet = re.sub("\s{2,}", " ", tweet)  # remove multiple spaces
    tweet = tweet.strip()
    return tweet


f = open("output.json", "r")
data = f.read()
data = data.split("\n")

formatted_data = []
for x in data:
    try:
        x = json.loads(x)
        each_entry = {}
        each_entry["username"] = x["username"]
        tweet = clean_tweet(x["tweet"])
        each_entry["tweet"] = tweet
        each_entry["hashtags"] = x["hashtags"]
        each_entry["likes_count"] = x["likes_count"]
        en_data += 1
        formatted_data.append(each_entry)
    except:
        continue

with open("formatted_output.json", "w") as fout:
    json.dump(formatted_data, fout)

