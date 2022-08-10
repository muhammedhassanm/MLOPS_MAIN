import os
import argparse
import yaml
import logging

def read_parameters(config_path):
    
    with open(config_path)as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path,data_source):
    config = read_parameters(config_path)
    print(config)

if __name__ =="__main__":
    # Find related codes in mlops_main
    args = argparse.ArgumentParser()
    default_config_path = os.path.join('config','params.yaml')
    args.add_argument("--config",default=default_config_path)
    args.add_argument("--datasource",default = None)
    
    parsed_args = args.parse_args()
    print(parsed_args.config)
    # print(parsed_args.data_source)
    main(config_path = parsed_args.config,data_source = parsed_args.datasource)
    