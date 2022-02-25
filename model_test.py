import argparse
from train_test import *
from utils.util import *
import pickle
from parse_config import ConfigParser

def main(config):
    test_data = get_user2item_test_data(config)
    testing(test_data, config)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KRED')

    parser.add_argument('-c', '--config', default="./config.yaml", type=str,
                        help='config file path (default: None)')
    parser.add_argument('-r', '--resume', default=None, type=str,
                        help='path to latest checkpoint (default: None)')
    parser.add_argument('-d', '--device', default=None, type=str,
                        help='indices of GPUs to enable (default: all)')

    config = ConfigParser.from_args(parser)
    main(config)