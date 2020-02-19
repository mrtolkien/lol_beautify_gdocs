import re
import joblib
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_service():
    credentials = None
    token_location = os.path.join(os.path.join(os.path.expanduser("~"), '.config', 'gsuite_api', 'token.pickle'))

    # The file token.pickle stores the user's access and refresh tokens, and is created
    # automatically when the authorization flow completes for the first time.
    if os.path.exists(token_location):
        credentials = joblib.load(token_location)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(os.path.join(os.path.expanduser("~"), '.config', 'gsuite_api', 'credentials.json')),
                'https://www.googleapis.com/auth/documents')
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        joblib.dump(credentials, token_location)

    return build('docs', 'v1', credentials=credentials)


def get_document_id(document_descriptor: str):
    """
    Parameter
    ----------
    document : str
        url or id of the document; must have write access by the authenticated user
    """
    id_regex = re.compile("[a-zA-Z0-9-_]{44}")

    if not id_regex.match(document_descriptor):
        document_id = id_regex.search(document_descriptor)[0]
    else:
        document_id = document_descriptor

    return document_id

##

