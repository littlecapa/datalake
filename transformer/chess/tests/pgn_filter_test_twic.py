import sys
sys.path.append('..')

from pgn_filter import PGN_Filter as pf

new_filter = pf("/Volumes/Data/DataLake/chess/pgn/twic1494.pgn", "/Volumes/Data/DataLake/chess/filtered")
new_filter.register_filter("2000++", "games2000plusplus.pgn")
new_filter.register_filter("2000+", "games2000plus.pgn")
new_filter.filter()
