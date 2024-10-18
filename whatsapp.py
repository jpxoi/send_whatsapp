import pywhatkit
import logging

# Set up logging to both console and file
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format the log messages
    handlers=[
        logging.FileHandler("whatsapp_log.txt"),  # Log to a file
    ]
)

# Function to send WhatsApp message to a contact
def send_message_to_contact(phone_number, message, time_hour, time_minute, wait_time, close_tab, close_wait_time):
    if not phone_number:
        logging.error("Phone number is required for sending to a contact.")
        return
    try:
        logging.info(f"Sending message to contact: {phone_number}")
        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, wait_time, close_tab, close_wait_time)
        logging.info("Message sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send message to contact: {e}")

# Function to send WhatsApp message to a group
def send_message_to_group(group_id, message, time_hour, time_minute, wait_time, close_tab, close_wait_time):
    if not group_id:
        logging.error("Group ID is required for sending to a group.")
        return
    try:
        logging.info(f"Sending message to group: {group_id}")
        pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, wait_time, close_tab, close_wait_time)
        logging.info("Message sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send message to group: {e}")

# Helper function to get input with a default value
def get_input_with_default(prompt, default_value, cast_func=str):
    user_input = input(f"{prompt} [{default_value}]: ")
    return cast_func(user_input) if user_input.strip() else default_value

# Input Mode Selection
mode = input("Enter mode ('contact' or 'group'): ").lower()

# Collect inputs based on the selected mode
if mode == "contact":
    phone_number = input("Enter phone number: ")
    group_id = ''  # Not needed for this mode
elif mode == "group":
    group_id = input("Enter group ID: ")
    phone_number = ''  # Not needed for this mode
else:
    logging.error("Invalid mode selected. Please choose either 'contact' or 'group'.")
    exit()  # Exit if an invalid mode is selected

# Collect shared inputs
message = input("Write the message here: ")
time_hour = int(input("Enter the hour (24-hour format): "))
time_minute = int(input("Enter the minute: "))

# Collect optional inputs with defaults
waiting_time_to_send = get_input_with_default("Enter waiting time to send (in seconds)", 15, int)
close_tab = get_input_with_default("Close tab after sending? (True/False)", True, lambda x: x.lower() == 'true')
waiting_time_to_close = get_input_with_default("Enter waiting time to close tab (in seconds)", 2, int)

mode = input("Enter mode ('contact' or 'group'): ").lower()

# Execution logic
if mode == "contact":
    send_message_to_contact(phone_number, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    send_message_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    logging.error("Invalid mode selected. Please choose either 'contact' or 'group'.")
