""" 
api.py
"""

from typing import Iterable
from flask import Flask, jsonify, make_response, request, Response

app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score() -> Response:
    """Score data using an imaginary machine learning model.
    This API endpoint expects a JSON payload with a field called `X`
    containing an iterable sequence of features to send to the model.
    This data is parsed into Python dict and made available via
    `request.json`
    If `X` cannot be found in the parsed JSON data, then an exception
    will be raised. Otherwise, it will return a JSON payload with the
    `score` field containing the model's prediction.
    """
    
    try:
        features = request.json['X']
        prediction = model_predict(features)
        return make_response(jsonify({'score': prediction}))
    except KeyError:
        raise RuntimeError('"X" cannot be found in JSON payload.')

def model_predict(x: Iterable[float]) -> Iterable[float]:
    """
    Dummy prediction function.
    """
    return x

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)