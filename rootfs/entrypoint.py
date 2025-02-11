#!/usr/bin/env python

from flask import Flask, request, Response
from detoxify import Detoxify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def detox():
    text = request.args.get('text')
    model_name = request.args.get('model', 'original-small')

    results = Detoxify('original-small').predict(text)

    allowed_models = ['multilingual', 'original-small', 'original']
    if model_name not in allowed_models:
        return Response(json.dumps({"error": "Invalid model name one of 'multilingual', 'original-small', 'original' has to be provided"}), status=400, mimetype='application/json')

    # Convert NumPy float32 to standard Python float
    try:
        model = Detoxify(model_name)
        results = model.predict(text)

        serializable_results = {}
        for key, value in results.items():
            serializable_results[key] = float(value)

        return Response(json.dumps(serializable_results), mimetype='application/json')

    except Exception as e: # Handle potential errors during prediction
        return Response(json.dumps({"error": str(e)}), status=500, mimetype='application/json') # Return error message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
