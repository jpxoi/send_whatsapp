import pywhatkit
import logging
import re

# Set up logging to both console and file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("whatsapp_log.txt"),
        # logging.StreamHandler() # Uncomment this line to also log to console
    ]
)

class WhatsAppMessageSender:
    def __init__(self):
        self.mode = None
        self.phone_number = None
        self.group_id = None
        self.message = None
        self.time_hour = None
        self.time_minute = None
        self.waiting_time_to_send = 15  # Default value
        self.close_tab = True  # Default value
        self.waiting_time_to_close = 2  # Default value

    def get_input_with_default(self, prompt, default_value, cast_func=str):
        """Helper method to get input with a default value."""
        user_input = input(f"{prompt} [{default_value}]: ")
        return cast_func(user_input) if user_input.strip() else default_value

    def validate_phone_number(self, phone_number):
        """Validate that the phone number is in a correct format."""
        pattern = r'^\+\d{1,15}$'  # Example for international format +[country code][number]
        if not re.match(pattern, phone_number):
            print("Invalid phone number format. Please use the international format (e.g., +1234567890).")
            return False
        return True
    
    def validate_time(self, hour, minute):
        """Validate that the hour is between 0-23 and the minute is between 0-59."""
        if not (0 <= hour <= 23):
            print("Hour must be between 0 and 23.")
            return False
        if not (0 <= minute <= 59):
            print("Minute must be between 0 and 59.")
            return False
        return True

    def collect_inputs(self):
        """Collect all necessary inputs from the user with interactive prompts and error handling."""
        print("\n=== WhatsApp Message Sender ===")
        
        # Mode selection
        while True:
            self.mode = input("\nEnter mode ('contact' to send a message to a contact, or 'group' to send to a group): ").lower()
            if self.mode in ['contact', 'group']:
                break
            else:
                print("Invalid mode. Please enter 'contact' or 'group'.")

        # Collect mode-specific inputs
        if self.mode == "contact":
            while True:
                self.phone_number = input("Enter phone number (e.g., +1234567890): ")
                if self.validate_phone_number(self.phone_number):
                    break
        elif self.mode == "group":
            self.group_id = input("Enter group ID: ")

        # Collect shared inputs
        self.message = input("\nWrite the message you want to send: ")

        # Collect time inputs with validation
        while True:
            try:
                self.time_hour = int(input("\nEnter the hour to send the message (24-hour format, 0-23): "))
                self.time_minute = int(input("Enter the minute to send the message (0-59): "))
                if self.validate_time(self.time_hour, self.time_minute):
                    break
            except ValueError:
                print("Please enter valid numbers for the time.")

        # Collect optional inputs with defaults
        self.waiting_time_to_send = self.get_input_with_default(
            "\nEnter waiting time before sending the message (in seconds)", 15, int
        )
        self.close_tab = self.get_input_with_default(
            "Close tab after sending? (True/False)", True, lambda x: x.lower() == 'true'
        )
        self.waiting_time_to_close = self.get_input_with_default(
            "Enter waiting time before closing the tab (in seconds)", 2, int
        )

    def send_message_to_contact(self):
        """Send a WhatsApp message to a contact."""
        try:
            logging.info(f"Sending message to contact: {self.phone_number}")
            print(f"\nSending message to contact: {self.phone_number}...")
            pywhatkit.sendwhatmsg(self.phone_number, self.message, self.time_hour, self.time_minute,
                                  self.waiting_time_to_send, self.close_tab, self.waiting_time_to_close)
            print("Message sent successfully!")
            logging.info("Message sent successfully!")
        except Exception as e:
            print(f"Failed to send message to contact: {e}")
            logging.error(f"Failed to send message to contact: {e}")

    def send_message_to_group(self):
        """Send a WhatsApp message to a group."""
        try:
            logging.info(f"Sending message to group: {self.group_id}")
            print(f"\nSending message to group: {self.group_id}...")
            pywhatkit.sendwhatmsg_to_group(self.group_id, self.message, self.time_hour, self.time_minute,
                                           self.waiting_time_to_send, self.close_tab, self.waiting_time_to_close)
            print("Message sent successfully!")
            logging.info("Message sent successfully!")
        except Exception as e:
            print(f"Failed to send message to group: {e}")
            logging.error(f"Failed to send message to group: {e}")

    def execute(self):
        """Main method to execute the message sending based on the selected mode."""
        if self.mode == "contact":
            self.send_message_to_contact()
        elif self.mode == "group":
            self.send_message_to_group()
        else:
            logging.error("Invalid mode selected during execution.")
            print("Error: Invalid mode during execution.")


# Instantiate the class and run the message sending process
if __name__ == "__main__":
    sender = WhatsAppMessageSender()
    sender.collect_inputs()
    sender.execute()
