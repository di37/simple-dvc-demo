## Read params
## Process
## Return Dataframe

import os, yaml, argparse
import pandas as pd

def read_params(config_path: str):
    '''
        Returns the configurations stored in yaml file.
    '''
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path: str):
    '''
        Returns the raw dataset. 
    '''
    config = read_params(config_path)
    data_path = config['data_source']['s3_source']
    sep = config['base']['sep']
    encoding = config['base']['encoding']
    df = pd.read_csv(data_path, sep=sep, encoding=encoding)
    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)