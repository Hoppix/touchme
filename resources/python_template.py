#!/usr/bin/env python3

"""A simple python script template."""

import os
import json
import logging
import argparse

DEBUG = os.getenv("DEBUG", False)
logging.getLogger().setLevel("DEBUG" if DEBUG else "INFO")

parser = argparse.ArgumentParser()
# index argument
parser.add_argument('filename')
# flag argument
parser.add_argument('-f', '--flag', required=False) 

def main():
    logging.debug("Hello logging!")
    # YOUR CODE HERE
    pass

if __name__ == "__main__":
    raise SystemExit(main())