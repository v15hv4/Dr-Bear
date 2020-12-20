<img src="https://media.discordapp.net/attachments/766879223897653272/790189284371202078/image-removebg-preview_1.png">

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



## Installation

TODO

## Implementation

TODO

### Real-time Data Fetching

TODO

### Web Application

<put screenshot>

We used a React front-end and a Flask back-end for the webapp. There are two main components, one that fetches and display the data, and one which has the Chatbot component. Data is taken from the Chatbot and given to the several API calls, which then undergo data parsing and are fetched to display to the user. When making the webapp, speed and comfort were our primary targets, and we did several optimizations for it.

### Sentiment Analysis

<img src="https://media.discordapp.net/attachments/766879223897653272/790164137497460757/Architecture-of-the-BERT-based-discriminator-model-Raw-texts-are-fed-into-the-model-to.png">

To check how the users of any platform react to a company's current status, we turn to Machine Learning techniques to process vast amounts of data rather rapidly. Since financial advice, if also considered *risky* by many, we have used a SOTA model from Deep Learning (a subset of Machine Learning) to subdue your anxieties about lousy advice. More specifically, we have obtained over 86% accuracy in detecting the right sentiments, which places the model well over the standard models, especially considering the speed it is expected to run under.
The model we have used in **DistilBERT**. Distill stands for a *distilled* version of the original model, **BERT**. BERT stands for Bidirectional Encoder Representations from Transformers. What this means is:
- **BiDirectional**: we consider bidirectional semantic and syntactic dependencies
- **Encoder Representations**: converts the sequence of words (be it a tweet or a Reddit comment) into a high dimensional single vector representation; in other words, it converts all the information from the entire sequence into a single vector.
- **Transformers**: Transformers are the current state of the model architectures used in NLP (Natural Language Processing), using highly parallel GPU architectures at the hardware level, which are miles better than LSTMs or Bi-LSTMS, which take up a lot of time.

Now, we could have used the original BERT model, but it's almost twice as large, taking nearly twice as much space and thus around twice the time to predict sentiments. *DistilBERT brings the same ideas from BERT and distills them, preserving most of the model accuracy but improving speed manifolds.* We have taken utmost care to make the model as speedy and compact as possible, and therefore used DistilBERT for our purpose.

Why the emphasis on space and speed? Well, not only is the model quite heavy, but it also takes some milliseconds to generate a prediction. We also consider the fact that the user request is generated on demand. We do not store anything beforehand (we cache for later), but the first runs shouldn't take time; after all, they determine whether the user will stay on our site. So we scrape Twitter and Reddit *on-demand* and analyze them, again, *on-demand*. We are thus able to produce highly relevant data and highly relevant insights at a fast speed.

### Chatbot



### Members

TODO

## Further Ideas

TODO
