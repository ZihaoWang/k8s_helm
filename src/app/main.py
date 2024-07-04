from joblib import load
import os
from typing import Tuple
from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(PATH, "../data/diabetes.csv")
MODEL_PATH = os.path.join(PATH, "../models/")


def get_latest_model() -> Tuple[object, str]:
    models = os.listdir(MODEL_PATH)
    models.sort()
    model_name = models[-1]
    model = load(MODEL_PATH + model_name)
    return model, model_name

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='ok')

@app.route("/predictions", methods=["GET"])
def index():
    data = np.array([8, 154, 78, 32, 0, 32.4, 0.443, 45]).reshape(1, -1)

    skmodel, model_name = get_latest_model()
    prediction = skmodel.predict(data)

    return jsonify({"name": model_name, "prediction": prediction.item()})


app.debug = True
app.run()
