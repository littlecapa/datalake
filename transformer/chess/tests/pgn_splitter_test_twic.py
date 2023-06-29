import sys
sys.path.append('..')

from pgn_splitter import PGN_Splitter as ps

new_splitter = ps("/Volumes/Data/DataLake/chess/pgn/", "twic1494.pgn", "split", 10000)
new_splitter.split()
