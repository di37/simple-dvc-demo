import os, argparse
from get_data import read_params, get_data


def load_and_save(config_path: str):
    """
    Loads the data from the data_given folder and saves it in
    appropriate format for further process.
    """
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    
    sep = config["base"]["sep"]
    index = config["base"]["index"]
    
    df.to_csv(raw_data_path, sep=sep, index=index, header=new_cols)


## Extra Comment
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(parsed_args.config)
