import argparse
import sys

sys.path.append('..')

from pgn_filter import PGN_Filter as pf


import logging.config
import logging
logger = logging.getLogger("root")

# Create an argument parser
parser = argparse.ArgumentParser()

# Define the expected command-line parameters
parser.add_argument("--input_file", help="")
parser.add_argument("--output_path", help="")
parser.add_argument("--output_file", help="")
parser.add_argument("--from_game", help="")
parser.add_argument("--to_game", help="")

# Parse the command-line arguments
args = parser.parse_args()

# Access the parameter values
param_input_file = args.input_file
param_output_path = args.output_path
param_output_file = args.output_file
param_from_value = int(args.from_game)
param_to_value = int(args.to_game)

print(f"Input-File Param: {param_input_file}")
print(f"Output-Path Param: {param_output_path}")
print(f"Output-File Param: {param_output_file}")
print(f"From Param: {param_from_value}")
print(f"To Param: {param_to_value}")

from pgn_filter_dc import PGN_Filter_DC as pfo

new_filter_obj = pfo(commentated = True, eco_from = "", eco_to = "", move_pattern = "")

for i in range(param_from_value, param_to_value):
    input_file_name = param_input_file.replace("_.pgn", "_" + str(i) + ".pgn")
    output_file_name = param_output_file.replace("_.pgn", "_" + str(i) + ".pgn")
    print(f"Input-File: {param_input_file} {input_file_name}")
    new_filter = pf(input_file_name, param_output_path, max_games = 10000000)
    new_filter.register_filter(new_filter_obj, output_file_name)
    print("Start Filter")
    new_filter.filter()
    print("End Filter")

sys.exit()