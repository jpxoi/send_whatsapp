from src.sender import WhatsAppMessageSender

sender = WhatsAppMessageSender(
    mode='contact',
    phone_number='+1234567890',
    message='Hello, this is a test message!',
    time_hour=10,
    time_minute=30
)
sender.execute()