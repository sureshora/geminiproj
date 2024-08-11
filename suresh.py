import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    environment = os.getenv('ENVIRONMENT', 'default')  # Default to 'default'
    return f"Hello from my Flask app! Running in {environment} environment."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 8080)))  # Port can be overridden