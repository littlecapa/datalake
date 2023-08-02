import subprocess

# Define the command to start the Python script with parameters

input_file = "/Volumes/Data/DataLake/chess/pgn/li_split/lichess_db_standard_rated_2023-02_.pgn"
output_path = "/Volumes/Data/DataLake/chess/filtered/split"
#output_path = "/Volumes/Data/DataLake/chess/filtered/split2"
output_file = "commentated_li_.pgn"

from_game = 252
to_game = 253
#from_game = 1000
#to_game = 1969
size = 50 

start = from_game
end = start + size

while True:
    if end > to_game:
        end = to_game
    command = ["python3", "extract_commentated_script.py", "--input_file", input_file, "--output_path", output_path, "--output_file", output_file, "--from_game", str(start), "--to_game", str(end) ]
    process = subprocess.Popen(command)
    start += size
    end += size
    if start > to_game:
        break
