# WhatsApp Message Sender

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Command-line Mode](#command-line-mode)
   - [Interactive Mode](#interactive-mode)
5. [Configuration](#configuration)
6. [Modules Overview](#modules-overview)
7. [Error Handling](#error-handling)
8. [Logging](#logging)

---

## Introduction

The **WhatsApp Message Sender** is a Python application designed to automate the process of sending WhatsApp messages through `pywhatkit`. It allows you to send messages to both individual contacts and groups. You can run it interactively through the console or directly pass arguments via command-line for automation. This tool also includes validation for inputs and logging for tracking message statuses.

---

## Features

- Send WhatsApp messages to contacts or groups.
- Command-line argument support for quick usage.
- Interactive input collection with validations and defaults.
- Logging system for tracking success or errors.
- Customizable parameters like waiting times and tab behavior.

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/jpxoi/send_whatsapp.git
    cd send-whatsapp
    ```

2. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure you have the following:
    - Python 3.x
    - `pywhatkit` (for sending WhatsApp messages)
    - `argparse` (for handling command-line arguments)
    - Other standard libraries (logging, re, etc.)

3. **WhatsApp Web**: Ensure that you are logged into WhatsApp Web on your default browser, as `pywhatkit` relies on it.

---

## Usage

You can use the program in two ways: via **command-line arguments** for automation or in an **interactive mode** where the program will guide you through input collection.

### Command-line Mode

You can directly send a message by passing parameters as command-line arguments.

**Example**:

```bash
python main.py --mode contact --phone +1234567890 --message "Hello, this is a test message!" --timehour 14 --timeminute 30
```

### Command-line Arguments

| Argument          | Type          | Description                                                                                       |
|-------------------|---------------|---------------------------------------------------------------------------------------------------|
| `--mode` or `-m`  | `str`         | Choose 'contact' or 'group' to send to a specific contact or WhatsApp group.                      |
| `--phone` or `-p` | `str`         | Phone number in international format (e.g., +1234567890). Required if mode is 'contact'.          |
| `--group` or `-g` | `str`         | Group ID for sending to a group. Required if mode is 'group'.                                     |
| `--message` or `-msg` | `str`     | The message content to send.                                                                     |
| `--timehour` or `-th` | `int`     | The hour (0-23) when the message should be sent.                                                  |
| `--timeminute` or `-tm` | `int`   | The minute (0-59) when the message should be sent.                                                |
| `--waitsend` or `-wts` | `int`    | (Optional) Waiting time before sending the message (default: 15 seconds).                         |
| `--closetab` or `-ct` | `bool`    | (Optional) Whether to close the browser tab after sending (default: True).                        |
| `--waitclose` or `-wtc` | `int`   | (Optional) Waiting time before closing the browser tab (default: 2 seconds).                      |

### Interactive Mode

If you run the program without arguments, it will prompt you interactively to input all required fields.

```bash
python main.py
```

The program will guide you through:

1. Selecting the mode (`contact` or `group`).
2. Inputting the phone number (for `contact`) or group ID (for `group`).
3. Writing the message to send.
4. Specifying the time (hour and minute).
5. Optionally modifying waiting times and whether to close the tab after sending.

---

## Configuration

You can modify default values for certain parameters (like waiting times) by editing `config.py`. This file contains all default settings used throughout the application.

```python
# config.py

DEFAULT_WAITING_TIME_TO_SEND = 15  # in seconds
DEFAULT_CLOSE_TAB = True
DEFAULT_WAITING_TIME_TO_CLOSE = 2  # in seconds
```

---

## Modules Overview

To keep the project modular and maintainable, the code is divided into different files:

1. **`main.py`**: The main entry point. Handles argument parsing and directs the flow between command-line and interactive modes.
2. **`sender.py`**: Contains the core logic for sending WhatsApp messages (either to contacts or groups).
3. **`input_handler.py`**: Manages input collection and validation for interactive mode.
4. **`utils.py`**: Helper functions, such as logging setup and validation of phone numbers and time.
5. **`config.py`**: Contains default values for waiting times and other customizable settings.

---

## Error Handling

1. **Phone Number Validation**:
    - The phone number must follow the international format `+1234567890`. If the format is invalid, the program will display an error and ask for a valid number.

2. **Time Validation**:
    - The hour must be between 0-23, and the minute between 0-59. If the time is outside these ranges, the program will display an error.

3. **Command-line Errors**:
    - If a required argument is missing (e.g., no phone number is provided in contact mode), the program will raise an error explaining the issue.

4. **Exception Handling**:
    - Any issues with sending messages (e.g., network problems or incorrect inputs) will be caught and logged, and the program will display a friendly error message.

---

## Logging

Logging is set up to keep track of all key events, such as:

- Sending messages.
- Validation errors.
- Any issues encountered during execution.

The logs are written to a file called `whatsapp_message_sender.log` in the same directory as the script.

You can modify the logging setup in `utils.py`:

```python
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("whatsapp_message_sender.log"),
            # logging.StreamHandler()  # Uncomment to log to the console as well
        ]
    )
```
