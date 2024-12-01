# Keystroke Logging Server

This repository contains a Flask-based web server for capturing and storing keystroke data sent from a client application. The data is stored both in memory (for short-term retrieval) and in a SQLite database (for persistent storage). This project also includes functionality to retrieve stored logs via a GET endpoint.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [API Endpoints](#api-endpoints)
5. [Security and Ethical Considerations](#security-and-ethical-considerations)
6. [Contributing](#contributing)
7. [License](#license)


## Overview

The server captures keystrokes sent from a client, stores them in a persistent SQLite database, and provides an API to retrieve the logged data. The primary use case for this project is for testing and educational purposes. 

### **Key Components**:
- **Flask Web Framework**: Used to create the REST API and handle HTTP requests.
- **SQLite Database**: Used to store keystroke data persistently.
- **Logging System**: Logs incoming requests for monitoring and troubleshooting purposes.
- **Keystroke Data**: Data is sent to the server from a client application, which includes the keystroke and timestamp.

## Features

1. **Keystroke Logging**: The server receives keystroke data in the form of a POST request containing a timestamp and the pressed key.
2. **Persistent Storage**: Keystrokes are saved to an SQLite database (`logs.db`).
3. **Retrieve Logs**: The server exposes a GET API endpoint to retrieve the logs in JSON format.
4. **Logging**: All received keystrokes are logged to both a file (`student_logs.txt`) and an SQLite database.
5. **Error Handling**: The server includes basic error handling for missing or malformed data.


## Setup Instructions

### Prerequisites

Before running this server, make sure you have the following:

1. **Python 3.x**: This server is written in Python. Download and install Python 3.x from [python.org](https://www.python.org/).
2. **Pip**: Make sure `pip` is installed for managing Python dependencies.

### Install Dependencies

To install the required dependencies, run the following commands in your terminal or command prompt:

# Clone the repository (if you haven't already)
git clone https://github.com/yourusername/keystroke-logging-server.git

# Change to the project directory
cd keystroke-logging-server

# Install required packages
pip install -r requirements.txt

The `requirements.txt` file should include the following dependencies:

Flask==2.1.1
sqlite3  # Usually included with Python, but if you have issues, you may need to install it manually.

### Running the Server

After installing the dependencies, you can run the Flask server with the following command:

python app.py

The server will start and listen for requests on `http://0.0.0.0:5000`. You can adjust the IP address and port number if needed.

### Database Initialization

The SQLite database will be automatically initialized the first time the server runs. The `init_db()` function ensures that the necessary table (`keystrokes`) is created in the database.

## API Endpoints

### POST `/logs`

This endpoint allows clients to send keystroke data to the server.

- **Request Body**: 
    - `key`: The key that was pressed (string, could be a special key like `Key.shift` or regular characters).
    - `timestamp`: The timestamp when the key was pressed (string in the format `YYYY-MM-DD HH:MM:SS`).

**Example Request:**

POST /logs HTTP/1.1
Content-Type: application/json

{
    "key": "a",
    "timestamp": "2024-12-01 12:34:56"
}

- **Response**:
    - `200 OK` if the data was successfully received and stored.
    - `400 Bad Request` if no data was received or the request is malformed.

**Example Response:**

{
    "status": "success"
}

### GET `/logs`

This endpoint allows clients to retrieve all the stored keystroke logs.

- **Response**: 
    - A list of JSON objects, each containing the `timestamp` and `key` of each logged keystroke.

**Example Response:**

[
    {
        "timestamp": "2024-12-01 12:34:56",
        "key": "a"
    },
    {
        "timestamp": "2024-12-01 12:34:57",
        "key": "b"
    }
]


## Security and Ethical Considerations

### **Security**
- **Sensitive Data**: Keystroke data can be sensitive. Ensure that you handle and store this data securely, using encryption if necessary.
- **Authentication**: Implement authentication and authorization if the server is exposed to the internet. Without proper security, the server could be misused.
- **Data Storage**: The current setup stores data in plaintext (both in the database and logs). In a production environment, consider encrypting sensitive information.
  
### **Ethical Concerns**
- **User Consent**: Always ensure that users are aware of and have consented to the logging of their keystrokes.
- **Legality**: Keystroke logging may be illegal in certain jurisdictions without explicit consent. Make sure that you are compliant with local laws regarding data collection and privacy.

### **Best Practices**
- Only use this code in controlled environments where consent has been explicitly obtained, and ensure compliance with privacy laws (such as GDPR, CCPA, etc.).

## Contributing

Contributions to this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a description of your changes.

Please follow best practices for commit messages and include tests when applicable.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [SQLite](https://www.sqlite.org/) for lightweight, file-based database management.
