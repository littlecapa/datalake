import sys
sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")

from pgn_filter import PGN_Filter as pf
logger.debug("Starting")
new_filter = pf("/Volumes/Data/DataLake/chess/pgn/little_li.pgn", "/Volumes/Data/DataLake/chess/filtered", max_games = 10000000)
new_filter.register_filter("Commentated", "commentated.pgn")
#new_filter.register_filter("Commentated", "commentated2000plus.pgn")
new_filter.filter()
