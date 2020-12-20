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

    pprint(flow_output)

    return "Nice"


if __name__ == "__main__":
    app.run(debug=True)
