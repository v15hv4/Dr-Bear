from flask import Flask, request
from pprint import pprint
from dialog import DialogFlow

app = Flask(__name__)
dflow = DialogFlow()


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
        company_field = flow_output.query_result.parameters.fields["company"]
        company = company_field.list_value.values[0].string_value
    except:
        company = None

    try:
        source_field = flow_output.query_result.parameters.fields["source"]
        source = source_field.list_value.values[0].string_value
    except:
        source = None

    response = {"message": message, "source": source, "company": company}
    return response


if __name__ == "__main__":
    app.run(debug=True)
