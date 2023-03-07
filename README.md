# Send WhatsApp Messages using Python
This Python code uses the pywhatkit module to send a WhatsApp message to a contact or a group at a specific time. The user can specify the recipient's phone number or group ID, the message to be sent, the time to send

## Requirements
* Python 3.6 or higher
* The `pywhatkit` module is required.

## Usage
1. Install the `pywhatkit` module using the command `pip install pywhatkit`.
2. Replace the placeholders for `phone_number`, `group_id`, and `message` with actual values for the recipient's phone number or group ID and the message to be sent.
3. Replace the placeholders for `time_hour`, `time_minute`, `waiting_time_to_send`, and `waiting_time_to_close` with actual values for the time to send the message, the waiting time to send the message, and the waiting time to close the browser tab.
4. Set the `mode` variable to `"contact"` to send the message to a contact or `"group"` to send the message to a group.
5. Run the code.

## Code Explanation
The code can be divided into several parts:

### Importing Modules
```python
import pywhatkit
```

This line of code imports the necessary `pywhatkit` module for the script to run.

### Setting Variables
```python
phone_numer = ''
group_id = ''
message = 'Write the message here'
time_hour = 14
time_minute = 50
waiting_time_to_send = 15
close_tab = True
waiting_time_to_close = 2

mode = "contact"
```
These lines of code set the variables for the recipient's phone number or group ID, the message to be sent, the time to send the message, the waiting time to send the message, and the waiting time to close the browser tab. Replace the placeholders with actual values.

The `mode` variable is set to `"contact"` by default. Change the variable value to `"group"` to send the message to a group.

### Sending a WhatsApp Message
```python
if mode == "contact":
    pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")
```

These lines of code use the `sendwhatmsg()` or `sendwhatmsg_to_group()` function from the `pywhatkit` module to send the message to the recipient. If `mode` is set to `"contact"`, the `sendwhatmsg()` function is called with the recipient's phone number as an argument. If `mode` is set to `"group"`, the `sendwhatmsg_to_group()` function is called with the group ID as an argument.

The function parameters include the message to be sent, the time to send the message, the waiting time to send the message, and the waiting time to close the browser tab. The `close_tab` parameter is set to `True` by default, which closes the browser tab after sending the message.