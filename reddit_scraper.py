#comments is a dictionary, keys are subreddits and each subreddit has a few top sentences

import urllib.request, json 
import re
from pprint import pprint

query = 'tesla'
subreddits = ['investing','personalfinance','cryptocurrency','securityanalysis','finance']
days = '7'
size = 100
comments = {}

for subreddit in subreddits:
    url = urllib.request.urlopen(f"https://api.pushshift.io/reddit/search/comment/?q={query}&subreddit={subreddit}&after={days}d&size={size}&fields=body,score&sort_type=score&sort=desc")
    data = json.loads(url.read().decode())
    data_list = data['data']
    data_list = data_list[:5]
    body = []
    for x in data_list:
        sentences = x['body'].split('\n')
        c = 0
        for sentence in sentences:
            if len(sentence)>50 and c<=2:
                body.append(sentence)
                c+=1
    comments[subreddit] =  body
