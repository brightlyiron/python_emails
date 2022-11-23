import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from utils.email.providers.base import BaseProvider

# django in settings.py
creds, _ = google.auth.default()
SENDER_EMAIL = "example@example.co.kr"


class GoogleProvider(BaseProvider):

    def send_email(self, content: str, receiver: str):
        """Create and insert a draft email.
           Print the returned draft's message and id.
           Returns: Draft object, including draft id and message meta data.

          Load pre-authorized user credentials from the environment.
          TODO(developer) - See https://developers.google.com/identity
          for guides on implementing OAuth2 for the application.
        """

        try:
            # create gmail api client
            service = build('gmail', 'v1', credentials=creds)

            message = EmailMessage()

            message.set_content(content)

            message['To'] = SENDER_EMAIL
            message['From'] = receiver
            message['Subject'] = 'Test google email'

            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            create_message = {
                'message': {
                    'raw': encoded_message
                }
            }
            # pylint: disable=E1101
            draft = service.users().drafts().create(userId="me",
                                                    body=create_message).execute()

            print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

        except HttpError as error:
            print(F'An error occurred: {error}')
            draft = None

        return draft
