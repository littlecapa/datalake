import sys
sys.path.append('..')

from pgn_splitter import PGN_Splitter as ps

new_splitter = ps("/Volumes/Data/DataLake/chess/pgn/", "lichess_db_standard_rated_2023-02.pgn", "li_split2", 1000000, 1000*1000000)
new_splitter.split()
