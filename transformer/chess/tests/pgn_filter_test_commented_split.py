import sys
sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")

from pgn_filter import PGN_Filter as pf
logger.debug("Starting")

from pgn_filter_dc import PGN_Filter_DC as pfo

new_filter_obj = pfo(commentated = True, eco_from = "", eco_to = "", move_pattern = "")

for i in range(200, 201):
    new_filter = pf("/Volumes/Data/DataLake/chess/pgn/li_split/lichess_db_standard_rated_2023-02_"+str(i)+".pgn", "/Volumes/Data/DataLake/chess/filtered/split", max_games = 10000000)
    new_filter.register_filter(new_filter_obj, "commentated_li_"+str(i)+".pgn")
    new_filter.filter()
