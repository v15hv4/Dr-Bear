<img src="https://media.discordapp.net/attachments/766879223897653272/790189284371202078/image-removebg-preview_1.png">

# DrBear 

> "Risk comes from not knowing what you're doing." - Warren Buffet

**DrBear** is an assistant for all your investing needs. DrBear recognizes how volatile the market is, and how the market is defined by the people in it. DrBear is a chatbot that brings in the latest news, data, tweets about the company you want to see, using Sentiment Analysis trained using a cutting-edge DistilBERT model to identify the health of a company.

- Use [this link](http://52.151.193.38/) to checkout the demo webapp. 
- Checkout [this video](https://youtu.be/8c3gqu8wNJg) for a working demo. 

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

<img src="https://media.discordapp.net/attachments/766879223897653272/790198169664749569/unknown.png?width=857&height=414">

### Introduction

DrBear is a chatbot assistant for finance news, discussions on forums, tweets and other such features. It uses Sentiment Analysis to predict the health of a company based on how people talk about it. It has a web-app which does real-time scraping and implementation of NLP techniques for the above.

### About Investing

Investing is a task that needs a lot of background about any company. While many trading softwares do a cursory linear regression, such methods are useless at best and misleading at worst. A more informed user needs an assistant that assists and gives the necessary information. The market after all, is made of people, and what people like, sells.

### Technologies Involved

We have used Python for data-fetching and the Machine Learning models that we used, using various libraries such as tensorflow, nltk, and employing use of Regex for data cleaning. Our web-app has a React frontend and a Flask backend, and is hosted on a Azure platform, employing Dialogflow from GCP libraries for our chatbot. Here is a basic explanation of how our model works:

<img src="https://media.discordapp.net/attachments/766879223897653272/790196156838969354/Untitled_Diagram.png">



# MVP

## Installation

To install the backend API:

> :warning: **Make sure you are using python3.6+**:

First create a virtual environment using `venv`. For `apt` package manager,
```bash
sudo apt install python3-venv

python3 -m venv .env
```

Activate the environment and install the required dependencies:

```bash
. .env/bin/activate
pip3 install -r requirements.txt
```

For configuring the chatbot, you need to setup an account at Dailogflow
and create a service accounts. Check "Setup Authentication" section
on the official [Dialogflow documentation](https://cloud.google.com/dialogflow/es/docs/quick/setup).

After obtaining the accounts details in `json` format, place it in 
the folder `Backend`.

To run the backedn,

```bash
cd Backend
python3 app.py
```

To run the Clientside, we use Nodejs:

Install the dependencies
```bash
cd Client

npm install
```

To run the webapp,

```bash
npm start
```


### Real-time Data Fetching

We fetched data from multiple sources, using freely available APIs, or scraping in the case of Tweets. The data fetched is sorted according to likes, score or relevancy, and the rate called is one that is limited, since we wanted a seamless experience. The data has been cleaned whenever required, for example, in tweets we have removed hashtags and usertags.

### Web Application

<img src="https://media.discordapp.net/attachments/766879223897653272/790201475749773312/unknown.png?width=861&height=414">

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

We used Google's DialogFlow platform, which helps us do NLU (Natural Language Understanding). Our end goal is to extract two things:
1. The name of the publically traded company
2. The source which the user wants to explore: be it Twitter or Reddit or the latest news articles

We complete this task by creating entities and intents. For entities, we have two kinds; as listed above. The name of the source was rather easy to handle, since its only one word. However, names of companies are not always restricted to one word; we have names like "Bank of America Corp" or "General Electric", and so on. We handle this by feeding lots of handwritten and handcrafted data; which is able to then capture the multi-word names of the companies.

After we have created entities, we turn to intents. We have one single intent, which extracts both the entities, from the user input. This information in then passed onto the webapp, for further handling. 

### Members

The team involved in the project comprises of [Kunwar Shaanjeet Singh Grover](https://github.com/Groverkss), [Vishva Saravanan](https://github.com/v15hv4), [Mayank Goel](https://github.com/MayankGoel28) and [Tanishq Chaudhary](https://github.com/SmartyPants042), respectively.

## Further Ideas

Further improving speed, and implementing algo-trading solutions to add more depth to our bot. Parameter tuning to improve our Model is also on our priority.
