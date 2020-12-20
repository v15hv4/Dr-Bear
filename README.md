<img src="https://media.discordapp.net/attachments/766879223897653272/790160774651314176/unknown.png">

# DrBear 

> "Risk comes from not knowing what you're doing." - Warren Buffet

**DrBear** is an assistant for all your investing needs. DrBear recognizes how volatile the market is, and how the market is defined by the people in it. DrBear is a chatbot that brings in the latest news, data, tweets about the company you want to see, using Sentiment Analysis trained using a cutting-edge DistilBERT model to identify the health of a company.

- Use [this link](todo) to checkout the demo webapp. 
- Checkout [this video](todo) for a working demo. 

Whenever you do something risky, have a Doctor nearby. DrBear is the doctor for your investing needs.

## Table of Contents

- [About](#About)
    - [About Investing](#About-Investing)
    - [Technologies Involved](#Technologies-Involved)
- [MVP](#MVP)
    - [Features](#Features)
    - [Installation](#Installation)
    - [Implementation](#Implementation)
      - [Real-time Data Fetching](#Real-time-Data-Fetching)
      - [Web Application](#Web-Application)
      - [Sentiment Analysis](#Sentiment-Analysis)
      - [Chatbot](#Chatbot)
- [Further Ideas](#Further-Ideas)
- [Members](#Members)
- [License](LICENSE)

## About


### Introduction

DrBear is a chatbot assistant for finance news, discussions on forums, tweets and other such features. It uses Sentiment Analysis to predict the health of a company based on how people talk about it. It has a web-app which does real-time scraping and implementation of NLP techniques for the above.

### About Investing

Investing is a task that needs a lot of background about any company. While many trading softwares do a cursory linear regression, such methods are useless at best and misleading at worst. A more informed user needs an assistant that assists and gives the necessary information. The market after all, is made of people, and what people like, sells.

### Technologies Involved

We have used Python for data-fetching and the Machine Learning models that we used, using various libraries such as tensorflow, nltk, and employing use of Regex for data cleaning. Our web-app has a React frontend and a Flask backend, and is hosted on a Azure platform, employing Dialogflow from GCP libraries for our chatbot.



# MVP

### Features

TODO

## Installation

TODO

## Implementation

TODO

### Real-time Data Fetching

TODO

### Web Application

TODO

### Sentiment Analysis

<img src="https://media.discordapp.net/attachments/766879223897653272/790164137497460757/Architecture-of-the-BERT-based-discriminator-model-Raw-texts-are-fed-into-the-model-to.png">

To check how the users of any platform react to a company's current status, we turn to Machine Learning techniques; able to preocess huge amuonts of data rather rapidly. Since financial advide if also condidered *risky* by many, we have used a SOTA model from Deep Learning (a subset of Machine Learning) to subdue your anxieties about bad advice. More specifically, we have obtained a whopping accuracy of over 86% in detecting the right sentiments, which palces the model well over the standard models. Now, what is this model?

The model we have used in **DistilBERT**. Distil stands for a *distilled* version of the original model, **BERT**. BERT stands for Bidirectional Encoder Representations from Transformers. What this means is:
- **BiDirectional**: we consider bidirectional semantic and syntactic dependencies
- **Encoder Representaions**: converts the sequence of words (be it a tweet or a reddit comment) into a high dimensional single vector representaion; in other words, it converts all the information from the entire sequence into a single vector.
- **Transformers**: No, it doesn't refer to Optimus Prime. Transformers are instead the current state of the model architectures used in NLP (natural Language Processing) making use of highly parallel GPU architectures at the hardware level, which are miles better than LSTMs or Bi-LSTMS, which take up a lot of time.

Now, we could have used the original BERT model, but its almost twice as large; taking almost twice as much space and thus around twice the time to predict sentiments. *DistilBERT takes the same ideas from BERT and distils them, preserving most of the model accuracy but improving speed manifolds.* We have taken utmost care to make the model as speedy and compact as possible, and therefore used DistilBERT for our purpose.

Why the emphasis on space and speed? Well, not only is the model quite heavy, but also takes some milliseconds to generate a prediction. We also consider the fact that the user request are generated on demand. We do not store anything before-hand (we cache for later) but the first runs shouldn't take time; after all they determine whether the user is going to stay on our site or not. So we scrape twitter and reddit *on-demand* and the analyse them, again, *on-deamand*. We are thus able to produce highly relevant data as well as highly relevant insights lightning fast.

### Chatbot

TODO

### Members

TODO

## Further Ideas

TODO
