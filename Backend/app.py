from flask import Flask, request
from pprint import pprint
from dialog import DialogFlow
from scrapper import Scrapper
from predict import predict_sentiment

app = Flask(__name__)
dflow = DialogFlow()
scrap = Scrapper()


@app.route("/chat/", methods=["POST"])
def chat():
    req_data = request.get_json()
    input_query = req_data["input"]

    try:
        flow_output = dflow.collect_intent(input_query)
    except Exception as error:
        pprint(error)
        return "Error"

    message = flow_output.query_result.fulfillment_messages[0].text.text[0]

    try:
        company_field = flow_output.query_result.parameters.fields["Company"]
        company = company_field.list_value.values[0].string_value
    except:
        company = None

    try:
        source_field = flow_output.query_result.parameters.fields["source"]
        source = source_field.list_value.values[0].string_value
    except:
        source = None

    raw_data = None
    if company is not None:
        if source == "reddit":
            raw_data = scrap.scrape_reddit(company)
            for key in raw_data.keys():
                predictions = predict_sentiment(raw_data[key])
                raw_data[key] = [
                    (sentence, int(prediction))
                    for sentence, prediction in zip(raw_data[key], predictions)
                ]
        elif source == "news":
            raw_data = scrap.scrape_news(company)
            sentences = [news_url["title"] for news_url in raw_data]
            predictions = predict_sentiment(sentences)
            for data, prediction in zip(raw_data, predictions):
                data["sentiment"] = int(prediction)
        elif source == "twitter":
            raw_data = scrap.scrape_twitter(company)
            sentences = [tweet_object["tweet"] for tweet_object in raw_data]
            predictions = predict_sentiment(sentences)
            for data, prediction in zip(raw_data, predictions):
                data["sentiment"] = int(prediction)

    response = {
        "message": message,
        "source": source,
        "data": raw_data,
        "company": company,
    }
    return response


if __name__ == "__main__":
    app.run(debug=True)
