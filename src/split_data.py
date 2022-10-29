# Split the raw data
# Save it in data/processed folder

from operator import index
import os, argparse
from random import random
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params


def split_and_saved_data(config_path: str):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    split_ratio = config["split_data"]["test_size"]

    random_state = config["base"]["random_state"]
    sep = config["base"]["sep"]
    index = config["base"]["index"]
    encoding = config["base"]["encoding"]

    df = pd.read_csv(raw_data_path, sep=sep)
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    ## Just for demonstration of this example project, we will not be
    ## Preprocessing object datatype column. So we will just drop it.
    train.drop(columns=["car_name"], inplace=True)
    test.drop(columns=["car_name"], inplace=True)

    train = train[~(train['horsepower'] == "?")]
    test = test[~(test['horsepower'] == "?")]

    train.to_csv(train_data_path, index=index, encoding=encoding)
    test.to_csv(test_data_path, index=index, encoding=encoding)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)
