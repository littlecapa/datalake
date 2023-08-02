import argparse
import sys

sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")
logger.debug("Started")

# Create an argument parser
parser = argparse.ArgumentParser()

# Define the expected command-line parameters
parser.add_argument("--param1", help="")
parser.add_argument("--param2", help="")

# Parse the command-line arguments
args = parser.parse_args()

# Access the parameter values
param1 = args.param1
param2 = int(args.param2)
print(f"Params: {param1} {param2}")

sys.exit()