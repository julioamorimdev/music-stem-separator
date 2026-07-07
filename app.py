from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
VERSION = "1.0.0"
LOADED_MODEL = "default-model"
ACCEPTED_FORMATS = [".txt", ".pdf", ".docx", ".doc", ".rtf"]


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint returning version and loaded model."""
    return jsonify({
        "status": "ok",
        "version": VERSION,
        "loaded_model": LOADED_MODEL
    }), 200


@app.route('/api/formats', methods=['GET'])
def list_formats():
    """Endpoint returning accepted file formats."""
    return jsonify({
        "formats": ACCEPTED_FORMATS
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
