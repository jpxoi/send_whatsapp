# CLI Usage Examples for WhatsApp Message Sender

This document provides examples of how to use the WhatsApp Message Sender application from the command line.

## Sending a Message to a Contact

To send a WhatsApp message to a specific contact, use the following command:

```bash
python -m main -m contact -p +1234567890 -msg "Hello, this is a test message!" -th 10 -tm 30
```

### Parameters

- `-m`, `--mode`: Specify the mode of sending. Options are `contact` or `group`.
- `-p`, `--phone`: Phone number in international format (e.g., `+1234567890`).
- `-msg`, `--message`: The message you want to send.
- `-th`, `--timehour`: Hour to send the message (0-23).
- `-tm`, `--timeminute`: Minute to send the message (0-59).
- `-wts`, `--waitsend`: Optional. Waiting time before sending the message in seconds (default: 15).
- `-ct`, `--closetab`: Optional. Whether to close the tab after sending (default: True).
- `-wtc`, `--waitclose`: Optional. Waiting time before closing the tab in seconds (default: 2).

## Sending a Message to a Group

To send a WhatsApp message to a group, use the following command:

```bash
python -m main -m group -g my_group_id -msg "Hello everyone!" -th 14 -tm 45
```

### Parameters

- `-m`, `--mode`: Specify the mode of sending. Options are `contact` or `group`.
- `-g`, `--group`: Group ID for the target group.
- `-msg`, `--message`: The message you want to send.
- `-th`, `--timehour`: Hour to send the message (0-23).
- `-tm`, `--timeminute`: Minute to send the message (0-59).
- `-wts`, `--waitsend`: Optional. Waiting time before sending the message in seconds (default: 15).
- `-ct`, `--closetab`: Optional. Whether to close the tab after sending (default: True).
- `-wtc`, `--waitclose`: Optional. Waiting time before closing the tab in seconds (default: 2).

## Interactive Mode

If no command-line arguments are provided, the application will enter interactive mode, allowing you to input the required parameters step by step.

```bash
python -m main
```

This mode will prompt you to enter the mode (contact or group), phone number, group ID, message, time to send, and other parameters interactively.

## Conclusion

You can combine these command-line options to suit your needs and automate the process of sending WhatsApp messages. For more details on each parameter, please refer to the code or the application's documentation.
