from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
from app.core.config import settings

class GmailService:
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    def __init__(self):
        self.creds = None

    def get_flow(self):
        """
        Creates a Flow instance from the stored client secrets.
        """
        # If running on Railway, we might need to load from env var string
        if settings.GOOGLE_CREDENTIALS_JSON:
            client_config = json.loads(settings.GOOGLE_CREDENTIALS_JSON)
            return Flow.from_client_config(
                client_config,
                scopes=self.SCOPES,
                redirect_uri=settings.GOOGLE_REDIRECT_URI
            )
        else:
            # Local fallback
            return Flow.from_client_secrets_file(
                'backend/credentials.json',
                scopes=self.SCOPES,
                redirect_uri=settings.GOOGLE_REDIRECT_URI
            )

    def build_service(self, user_tokens: dict):
        """
        Builds the Gmail API service using user's tokens.
        """
        creds = Credentials.from_authorized_user_info(user_tokens, self.SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
             creds.refresh(Request())
             
        service = build('gmail', 'v1', credentials=creds)
        return service, creds

gmail_service = GmailService()
