import logging
import re

def setup_logging():
    """Sets up logging to both file and optionally console."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("whatsapp_message_sender.log"),
            # logging.StreamHandler()  # Uncomment to log to console as well
        ]
    )

def validate_phone_number(phone_number):
    """Validate phone number format (international +countrycode)."""
    pattern = r'^\+\d{1,15}$'
    if not re.match(pattern, phone_number):
        print("Invalid phone number format. Use +1234567890.")
        return False
    return True

def validate_time(hour, minute):
    """Validate hour and minute range."""
    if not (0 <= hour <= 23):
        print("Hour must be between 0 and 23.")
        return False
    if not (0 <= minute <= 59):
        print("Minute must be between 0 and 59.")
        return False
    return True
