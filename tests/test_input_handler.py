import unittest
from unittest.mock import patch, MagicMock

from src.input_handler import collect_inputs  # Adjust the import based on your project structure
from src.sender import WhatsAppMessageSender  # Adjust the import based on your project structure
from src.utils import validate_phone_number, validate_time  # Assuming these are available in utils

class TestInputHandler(unittest.TestCase):

    def setUp(self):
        """Set up a WhatsAppMessageSender instance before each test."""
        self.sender = WhatsAppMessageSender()

    @patch('builtins.input', side_effect=[
        'contact',                 # mode
        '+1234567890',            # phone number
        'Hello, this is a test!', # message
        '10',                      # hour
        '30',                      # minute
        '15',                      # waiting time to send
        'True',                    # close tab
        '2'                        # waiting time to close
    ])
    @patch('src.utils.validate_phone_number', return_value=True)  # Mock validation to always pass
    @patch('src.utils.validate_time', return_value=True)          # Mock time validation to always pass
    def test_collect_inputs_contact_mode(self, mock_validate_phone, mock_validate_time, mock_input):
        """Test the input collection for contact mode."""
        collect_inputs(self.sender)
        
        self.assertEqual(self.sender.mode, 'contact')
        self.assertEqual(self.sender.phone_number, '+1234567890')
        self.assertEqual(self.sender.message, 'Hello, this is a test!')
        self.assertEqual(self.sender.time_hour, 10)
        self.assertEqual(self.sender.time_minute, 30)
        self.assertEqual(self.sender.waiting_time_to_send, 15)
        self.assertTrue(self.sender.close_tab)
        self.assertEqual(self.sender.waiting_time_to_close, 2)

    @patch('builtins.input', side_effect=[
        'group',                  # mode
        'my_group_id',           # group ID
        'Hello group, this is a test!',  # message
        '14',                    # hour
        '45',                    # minute
        '30',                    # waiting time to send
        'False',                # close tab
        '5'                      # waiting time to close
    ])
    @patch('src.utils.validate_time', return_value=True)          # Mock time validation to always pass
    def test_collect_inputs_group_mode(self, mock_validate_time, mock_input):
        """Test the input collection for group mode."""
        collect_inputs(self.sender)
        
        self.assertEqual(self.sender.mode, 'group')
        self.assertEqual(self.sender.group_id, 'my_group_id')
        self.assertEqual(self.sender.message, 'Hello group, this is a test!')
        self.assertEqual(self.sender.time_hour, 14)
        self.assertEqual(self.sender.time_minute, 45)
        self.assertEqual(self.sender.waiting_time_to_send, 30)
        self.assertFalse(self.sender.close_tab)
        self.assertEqual(self.sender.waiting_time_to_close, 5)

if __name__ == '__main__':
    unittest.main()
