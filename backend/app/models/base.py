from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    # Store refresh token encrypted or securely. 
    # For this MVP, we might store it directly but production requires encryption.
    google_refresh_token = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("Transaction", back_populates="owner")

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String, index=True) # e.g., "Banco BHD"
    last_four = Column(String, index=True) # "1234"
    user_id = Column(Integer, ForeignKey("users.id"))
    
    transactions = relationship("Transaction", back_populates="card")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="DOP")
    merchant = Column(String, index=True)
    date = Column(DateTime, index=True)
    category = Column(String, index=True, nullable=True) # Food, Transport, etc.
    description = Column(Text, nullable=True)
    
    # Metadata
    email_id = Column(String, unique=True) # Gmail Message ID to prevent dupes
    is_payment = Column(Boolean, default=False) # True if it's a payment TO the card
    
    owner_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))

    owner = relationship("User", back_populates="items")
    card = relationship("Card", back_populates="transactions")

class ParsingRule(Base):
    """
    regex patterns to parse emails from specific banks.
    """
    __tablename__ = "parsing_rules"
    
    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String, unique=True)
    sender_email = Column(String) # alerts@banco.com
    subject_contains = Column(String) # "Consumo Tarjeta"
    
    # Regex Patterns
    body_pattern = Column(String) # Regex with named groups (?P<amount>...), (?P<merchant>...)
