#!/usr/bin/env python

import os
from flask import Flask, request, Response
from detoxify import Detoxify
import json
import gc

app = Flask(__name__)

# Initialize models outside the request handler
# Model loading based on environment variable
MODEL_NAME = os.environ.get("DETOXIFY_MODEL", "original-small")  # Default to original-small
ALLOWED_MODELS = ['multilingual', 'original-small', 'original']

if MODEL_NAME not in ALLOWED_MODELS:
    raise ValueError(f"Invalid model name: {MODEL_NAME}. Must be one of {ALLOWED_MODELS}")

try:
    model = Detoxify(MODEL_NAME)
    print(f"Model '{MODEL_NAME}' loaded successfully.")  # Confirmation message
except Exception as e:
    print(f"Error loading model '{MODEL_NAME}': {e}") #Print Error Message
    exit(1) #Exit if model load fails

@app.route('/', methods=['GET'])
def detox():
    text = request.args.get('text')

    try:
        results = model.predict(text)

        serializable_results = {}
        for key, value in results.items():
            serializable_results[key] = float(value)

        return Response(json.dumps(serializable_results), mimetype='application/json')

    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500, mimetype='application/json')

    finally:
        gc.collect()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)