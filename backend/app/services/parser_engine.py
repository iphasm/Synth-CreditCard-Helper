import re
from typing import Optional, Dict
from datetime import datetime

class ParserEngine:
    def parse_transaction(self, email_body: str, sender: str, subject: str) -> Optional[Dict]:
        """
        Detects which bank the email is from and applies the corresponding regex rules.
        For MVP, we hardcode a rule for 'Banco Example'.
        """
        
        # Example Rule for "Banco BHD" (Mock)
        # Subject: Confirmo Transaccion
        # Body: ... consumo de RD$1,500.00 en UBER EATS con tarjeta terminada en 1234 el 2026-01-11 ...
        
        if "banco" in sender.lower() or "banco" in subject.lower():
            # Mock Regex Pattern
            # Amount: RD$ followed by digits and commas/dots
            amount_pattern = r"RD\$([\d,]+\.\d{2})"
            merchant_pattern = r"en\s+([A-Z0-9\s]+?)\s+con"
            card_pattern = r"terminada\s+en\s+(\d{4})"
            
            amount_match = re.search(amount_pattern, email_body)
            merchant_match = re.search(merchant_pattern, email_body)
            card_match = re.search(card_pattern, email_body)
            
            if amount_match and merchant_match:
                return {
                    "amount": float(amount_match.group(1).replace(",", "")),
                    "merchant": merchant_match.group(1).strip(),
                    "card_last_four": card_match.group(1) if card_match else "XXXX",
                    "date": datetime.utcnow(), # Ideally parse date from email
                    "currency": "DOP"
                }
        
        return None

parser_engine = ParserEngine()
