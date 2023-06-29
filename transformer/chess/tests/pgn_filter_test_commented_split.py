import sys
sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")

from pgn_filter import PGN_Filter as pf
logger.debug("Starting")

for i in range(2, 200):
    new_filter = pf("/Volumes/Data/DataLake/chess/pgn/li_split/lichess_db_standard_rated_2023-02_"+str(i)+".pgn", "/Volumes/Data/DataLake/chess/filtered/split", max_games = 10000000)
    new_filter.register_filter("Commentated", "commentated_li_"+str(i)+".pgn")
    new_filter.filter()
