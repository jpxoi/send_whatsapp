import argparse
from sender import WhatsAppMessageSender
from input_handler import collect_inputs

def main():
    # Set up argument parser for command-line arguments
    parser = argparse.ArgumentParser(description="Send WhatsApp messages to a contact or group via command line.")
    
    parser.add_argument('-m', '--mode', choices=['contact', 'group'], help="Select mode: 'contact' or 'group'.")
    parser.add_argument('-p', '--phone', help="Phone number in international format (e.g., +1234567890) for contact mode.")
    parser.add_argument('-g', '--group', help="Group ID for group mode.")
    parser.add_argument('-msg', '--message', help="Message to send.")
    parser.add_argument('-th', '--timehour', type=int, help="Hour to send the message (0-23).")
    parser.add_argument('-tm', '--timeminute', type=int, help="Minute to send the message (0-59).")
    parser.add_argument('-wts', '--waitsend', type=int, default=15, help="Waiting time before sending the message in seconds.")
    parser.add_argument('-ct', '--closetab', type=bool, default=True, help="Whether to close the tab after sending.")
    parser.add_argument('-wtc', '--waitclose', type=int, default=2, help="Waiting time before closing the tab in seconds.")
    
    args = parser.parse_args()

    if args.mode:
        # Command-line mode
        sender = WhatsAppMessageSender(
            mode=args.mode,
            phone_number=args.phone,
            group_id=args.group,
            message=args.message,
            time_hour=args.timehour,
            time_minute=args.timeminute,
            waiting_time_to_send=args.waitsend,
            close_tab=args.closetab,
            waiting_time_to_close=args.waitclose
        )
        sender.execute()
    else:
        # Interactive mode
        sender = WhatsAppMessageSender()
        collect_inputs(sender)  # Interactive input collection
        sender.execute()


if __name__ == "__main__":
    main()
