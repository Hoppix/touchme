#!/usr/bin/env python3

import os
import logging
import argparse
import src.filechooser as filechooser

logging.getLogger().setLevel(os.getenv("TOUCHME_LOG_LEVEL", "DEBUG"))

parser = argparse.ArgumentParser(
                    prog = 'touchme',
                    description="Utility to create a new script based on templates",
                    epilog = 'Type: touchme followed by a filename, example - touchme test.sh or via flag touchme -f test.sh')

parser.add_argument('filename')
parser.add_argument('-f', '--file', required=False) 
parser.add_argument('-d', '--debug', required=False, action='store_true', default=False) 

def main():
    args = parser.parse_args()
    debug = args.debug
    current_directory = os.getcwd()
    filename = args.filename or args.file

    if debug:
        logging.getLogger().setLevel("DEBUG")


    logging.info(f"Creating new script in {current_directory} with name {filename}")
    full_path = f"{current_directory}/{filename}"
    template = filechooser.get_template(filename)

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w+') as fp:
            fp.write(template)
            pass
    except Exception as e:
        logging.error(f"File: {filename} could not be created. For more info use the -d / --debug option")
        logging.debug(f"File: {filename} could not be created. Error: {e}")

    if not os.path.isfile(full_path):
        logging.error(f"File: {filename} does not exsist. Full path: {full_path}")
        return -1

    
if __name__ == "__main__":
    logging.info("Running touchme as python script")
    main()