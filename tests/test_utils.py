import unittest
from unittest.mock import patch, MagicMock
import os
from src.utils import setup_logging, validate_phone_number, validate_time  # Adjust the import based on your project structure

class TestUtils(unittest.TestCase):

    def test_setup_logging(self):
        """Test the setup_logging function."""
        setup_logging()

        # Check if the log file was created
        self.assertTrue(os.path.exists("whatsapp_message_sender.log"))
        
        # Clean up after test
        os.remove("whatsapp_message_sender.log")

    def test_validate_phone_number_valid(self):
        """Test valid phone number."""
        valid_number = "+1234567890"
        result = validate_phone_number(valid_number)
        self.assertTrue(result)

    def test_validate_phone_number_invalid(self):
        """Test invalid phone number."""
        invalid_number = "1234567890"
        result = validate_phone_number(invalid_number)
        self.assertFalse(result)

    def test_validate_time_valid(self):
        """Test valid hour and minute."""
        result = validate_time(10, 30)
        self.assertTrue(result)

    def test_validate_time_invalid_hour(self):
        """Test invalid hour."""
        result = validate_time(25, 30)
        self.assertFalse(result)

    def test_validate_time_invalid_minute(self):
        """Test invalid minute."""
        result = validate_time(10, 70)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
