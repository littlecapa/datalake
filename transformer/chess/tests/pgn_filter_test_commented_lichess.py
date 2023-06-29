import sys
sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")

from pgn_filter import PGN_Filter as pf
logger.debug("Starting")
new_filter = pf("/Volumes/Data/DataLake/chess/pgn/lichess_db_standard_rated_2023-02.pgn", "/Volumes/Data/DataLake/chess/filtered")
new_filter.register_filter("Commentated", "commentated_li.pgn")
#new_filter.register_filter("Commentated", "commentated2000plus.pgn")
new_filter.filter()
