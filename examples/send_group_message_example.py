from src.sender import WhatsAppMessageSender

sender = WhatsAppMessageSender(
    mode='group',
    group_id='my_group_id',
    message='Hello everyone!',
    time_hour=14,
    time_minute=45
)
sender.execute()
