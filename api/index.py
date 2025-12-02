import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/api')
@app.route('/api/v1')
def index():
    return jsonify({
        "status": "ok",
        "message": "Flask app is running",
        "env_check": {
            "PROD_DB_set": bool(os.getenv('PROD_DB')),
            "JWT_SECRET_KEY_set": bool(os.getenv('JWT_SECRET_KEY')),
            "PROD_DB_length": len(os.getenv('PROD_DB', ''))
        }
    })

# For Vercel serverless
if __name__ != '__main__':
    # This is the entry point for Vercel
    application = app
