from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.services.gmail_service import gmail_service
# from app.db.session import get_db 
# from app.models.base import User
import json

router = APIRouter()

@router.get("/login")
def login():
    flow = gmail_service.get_flow()
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    # Ideally store 'state' in session to validate later
    return RedirectResponse(authorization_url)

@router.get("/callback")
def callback(request: Request, code: str):
    # db: Session = Depends(get_db)
    flow = gmail_service.get_flow()
    flow.fetch_token(code=code)
    
    creds = flow.credentials
    
    # Check if user exists or create new
    # user_email = ... (fetch from google userinfo endpoint if needed)
    
    # Store creds.to_json() in DB for this user
    
    return {"message": "Authenticated successfully", "creds_preview": json.loads(creds.to_json())}
