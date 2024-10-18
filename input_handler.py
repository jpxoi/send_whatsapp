from utils import validate_phone_number, validate_time

def collect_inputs(sender):
    """Interactive input collection for WhatsAppMessageSender"""
    print("\n=== WhatsApp Message Sender ===")

    # Mode selection
    while True:
        sender.mode = input("Enter mode ('contact' to send to a contact, 'group' to send to a group): ").lower()
        if sender.mode in ['contact', 'group']:
            break
        print("Invalid mode. Please enter 'contact' or 'group'.")

    # Mode-specific inputs
    if sender.mode == "contact":
        while True:
            sender.phone_number = input("Enter phone number (+1234567890): ")
            if validate_phone_number(sender.phone_number):
                break
    elif sender.mode == "group":
        sender.group_id = input("Enter group ID: ")

    # Common inputs
    sender.message = input("Write the message you want to send: ")

    # Time inputs with validation
    while True:
        try:
            sender.time_hour = int(input("Enter the hour to send (0-23): "))
            sender.time_minute = int(input("Enter the minute to send (0-59): "))
            if validate_time(sender.time_hour, sender.time_minute):
                break
        except ValueError:
            print("Please enter valid numbers for the time.")

    # Optional inputs
    sender.waiting_time_to_send = int(input("Waiting time before sending (seconds) [15]: ") or 15)
    sender.close_tab = input("Close tab after sending? (True/False) [True]: ").lower() in ['true', 't', '']
    sender.waiting_time_to_close = int(input("Time to wait before closing tab (seconds) [2]: ") or 2)
