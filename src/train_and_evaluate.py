# load the train and test
# train algo
# save the metrices, params
import os, warnings, sys, argparse, json, joblib
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train_and_evaluate(config_path: str):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]

    sep = config["base"]["sep"]
    encoding = config["base"]["encoding"]
    random_state = config["base"]["random_state"]

    params = config["estimators"]["ElasticNet"]["params"]
    alpha = params["alpha"]
    l1_ratio = params["l1_ratio"]

    target = [config["base"]["target_col"]]

    model_dir = config["save_model"]["model_dir"]
    model_name = config["save_model"]["model_name"]

    train_df = pd.read_csv(train_data_path, sep=sep, encoding=encoding)
    test_df = pd.read_csv(test_data_path, sep=sep, encoding=encoding)

    ## target
    train_y = train_df[target]
    test_y = test_df[target]

    ## Input Features
    train_x = train_df.drop(columns=target)
    test_x = test_df.drop(columns=target)

    # Model Instantiation
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)

    # Fitting the Model
    lr.fit(train_x, train_y)

    # Model Evaluation
    predicted_qualities = lr.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    # Saving Evaluation Metrics and Hyperparameters
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]
    indent_file = config["reports"]["indent"]

    with open(scores_file, "w") as f:
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        json.dump(scores, f, indent=indent_file)

    with open(params_file, "w") as f:
        params = {
            "alpha": rmse,
            "l1_ratio": mae,
        }
        json.dump(params, f, indent=indent_file)

    model_path = os.path.join(model_dir, model_name)
    joblib.dump(lr, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
