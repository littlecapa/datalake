import sys
sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")

from pgn_filter_kkrr import PGN_Filter_KKRR as pf

for i in range(100,200):
    new_filter = pf("/Volumes/Data/DataLake/chess/filtered/eval_mate/commentated_li_"+str(i)+".pgn", "/Volumes/Data/DataLake/chess/filtered/eval_mate/kkrr", max_games = 10000000)
    new_filter.filter()
