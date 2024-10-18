import pywhatkit
import logging
from src.utils import setup_logging

setup_logging()  # Configure logging

class WhatsAppMessageSender:
    def __init__(self, mode=None, phone_number=None, group_id=None, message=None, time_hour=None, time_minute=None,
                 waiting_time_to_send=15, close_tab=True, waiting_time_to_close=2):
        self.mode = mode
        self.phone_number = phone_number
        self.group_id = group_id
        self.message = message
        self.time_hour = time_hour
        self.time_minute = time_minute
        self.waiting_time_to_send = waiting_time_to_send
        self.close_tab = close_tab
        self.waiting_time_to_close = waiting_time_to_close

    def send_message_to_contact(self):
        """Send a WhatsApp message to a contact."""
        try:
            logging.info(f"Sending message to contact: {self.phone_number}")
            pywhatkit.sendwhatmsg(
                self.phone_number, self.message, self.time_hour, self.time_minute,
                self.waiting_time_to_send, self.close_tab, self.waiting_time_to_close
            )
            logging.info("Message sent successfully!")
        except Exception as e:
            logging.error(f"Failed to send message to contact: {e}")

    def send_message_to_group(self):
        """Send a WhatsApp message to a group."""
        try:
            logging.info(f"Sending message to group: {self.group_id}")
            pywhatkit.sendwhatmsg_to_group(
                self.group_id, self.message, self.time_hour, self.time_minute,
                self.waiting_time_to_send, self.close_tab, self.waiting_time_to_close
            )
            logging.info("Message sent successfully!")
        except Exception as e:
            logging.error(f"Failed to send message to group: {e}")

    def execute(self):
        """Execute the message sending based on the selected mode."""
        if self.mode == "contact":
            self.send_message_to_contact()
        elif self.mode == "group":
            self.send_message_to_group()
