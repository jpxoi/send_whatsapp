import unittest
from unittest.mock import patch, MagicMock
import logging

from src.sender import WhatsAppMessageSender  # Adjust the import based on your project structure

class TestWhatsAppMessageSender(unittest.TestCase):
    
    def setUp(self):
        """Set up test variables before each test."""
        self.sender_contact = WhatsAppMessageSender(
            mode="contact",
            phone_number="+1234567890",
            message="Hello, this is a test message.",
            time_hour=10,
            time_minute=30
        )
        self.sender_group = WhatsAppMessageSender(
            mode="group",
            group_id="my_group_id",
            message="Hello group, this is a test message.",
            time_hour=10,
            time_minute=30
        )

    @patch('pywhatkit.sendwhatmsg')  # Mocking the sendwhatmsg method
    def test_send_message_to_contact(self, mock_sendwhatmsg):
        """Test sending a message to a contact."""
        mock_sendwhatmsg.return_value = None  # Mock return value
        self.sender_contact.send_message_to_contact()
        mock_sendwhatmsg.assert_called_once_with(
            self.sender_contact.phone_number,
            self.sender_contact.message,
            self.sender_contact.time_hour,
            self.sender_contact.time_minute,
            self.sender_contact.waiting_time_to_send,
            self.sender_contact.close_tab,
            self.sender_contact.waiting_time_to_close
        )
        logging.info("send_message_to_contact test passed.")

    @patch('pywhatkit.sendwhatmsg_to_group')  # Mocking the sendwhatmsg_to_group method
    def test_send_message_to_group(self, mock_sendwhatmsg_to_group):
        """Test sending a message to a group."""
        mock_sendwhatmsg_to_group.return_value = None  # Mock return value
        self.sender_group.send_message_to_group()
        mock_sendwhatmsg_to_group.assert_called_once_with(
            self.sender_group.group_id,
            self.sender_group.message,
            self.sender_group.time_hour,
            self.sender_group.time_minute,
            self.sender_group.waiting_time_to_send,
            self.sender_group.close_tab,
            self.sender_group.waiting_time_to_close
        )
        logging.info("send_message_to_group test passed.")

    @patch('pywhatkit.sendwhatmsg')  # Mocking for execute method
    def test_execute_contact_mode(self, mock_sendwhatmsg):
        """Test the execute method for contact mode."""
        mock_sendwhatmsg.return_value = None  # Mock return value
        self.sender_contact.execute()
        mock_sendwhatmsg.assert_called_once()  # Ensure the send_message_to_contact method was called

    @patch('pywhatkit.sendwhatmsg_to_group')  # Mocking for execute method
    def test_execute_group_mode(self, mock_sendwhatmsg_to_group):
        """Test the execute method for group mode."""
        mock_sendwhatmsg_to_group.return_value = None  # Mock return value
        self.sender_group.execute()
        mock_sendwhatmsg_to_group.assert_called_once()  # Ensure the send_message_to_group method was called

if __name__ == '__main__':
    unittest.main()
