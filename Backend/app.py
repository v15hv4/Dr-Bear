from flask import Flask, request
from pprint import pprint
from dialog import DialogFlow
from scrapper import Scrapper
from predict import predict_sentiment

# Flask app
app = Flask(__name__)

# DialogFlow handler
dflow = DialogFlow()

# Scrapping functions handler
scrap = Scrapper()


@app.route("/chat/", methods=["POST"])
def chat():
    """API point handeling chatbot requests
    
    Args:
        Json input from via POST request
        Request should contain 'input' field
        containing chatbot qery

    Returns:
        JSON response:
        {
            "message": message,
            "source": source-to-scrap-data-from,
            "data": data-relavent-to-source,
            "company": company-name,
        }
    """
    req_data = request.get_json()
    input_query = req_data["input"]

    # Get analysis from diagnolflow
    try:
        flow_output = dflow.collect_intent(input_query)
    except Exception as error:
        pprint(error)
        return "Error"

    # Extract message from DiagnolFlow Response
    message = flow_output.query_result.fulfillment_messages[0].text.text[0]

    # Extract company from DiagnolFlow Response
    try:
        company_field = flow_output.query_result.parameters.fields["Company"]
        company = company_field.list_value.values[0].string_value
    except:
        company = None

    # Extract source from DiagnolFlow Response
    try:
        source_field = flow_output.query_result.parameters.fields["source"]
        source = source_field.list_value.values[0].string_value
    except:
        source = None

    # Scrape data from corresponding source and do sentiment analysis on it
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

    # Return response back to frontend
    response = {
        "message": message,
        "source": source,
        "data": raw_data,
        "company": company,
    }
    return response


if __name__ == "__main__":
    app.run()
