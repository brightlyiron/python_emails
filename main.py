import os

from utils.email import Email

CREDENTIAL_PATH = "/your/full-path/credentials.json"
os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', CREDENTIAL_PATH)
RECEIVER_EMAIL = "example@example.com"
CONTENT = "test"

if __name__ == '__main__':
    email_client = Email()
    email_client.send_email(CONTENT, RECEIVER_EMAIL)
