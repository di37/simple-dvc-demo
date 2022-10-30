from src.get_data import read_params
import joblib
import os
import numpy as np

params_path = "params.yaml"


def predict(data):
    config = read_params(params_path)
    model_dir_path = os.path.join(
        config["save_model"]["model_dir"], config["save_model"]["model_name"]
    )
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    return round(float(prediction[0]), 2)


def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try again"}
        return error
