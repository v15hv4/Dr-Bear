import dialogflow
from google.api_core.exceptions import InvalidArgument
import os


class DialogFlow:
    """Class abstracting dialogflow output details"""

    def __init__(self):
        self.DIALOGFLOW_PROJECT_ID = "drbear-dydw"
        self.DIALOGFLOW_LANGUAGE_CODE = "en-US"
        self.SESSION_ID = "9999999999"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./secrets.json"

    def collect_intent(self, raw_query):
        """Collections intents from dialogflow by passing a query
        
        Args:
            raw_query: Query to process on dialogflow

        Returns:
            DialogFlow Intents Response object
        """
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(
            self.DIALOGFLOW_PROJECT_ID, self.SESSION_ID
        )

        text_input = dialogflow.types.TextInput(
            text=raw_query, language_code=self.DIALOGFLOW_LANGUAGE_CODE
        )
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(
                session=session, query_input=query_input
            )
        except InvalidArgument:
            raise

        return response
