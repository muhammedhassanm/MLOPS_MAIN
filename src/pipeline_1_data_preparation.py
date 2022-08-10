import os
import argparse
import yaml
import logging

if __name__ =="__main__":
    # Find related codes in mlops_main
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--data_source",default = None)
    
    parsed_args = args.parse_args()
    print(parsed_args.config)
    print(parsed_args.data_source)
    