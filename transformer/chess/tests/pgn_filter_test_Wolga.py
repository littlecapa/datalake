import sys
sys.path.append('..')

import logging.config
import logging
logger = logging.getLogger("root")

from pgn_filter import PGN_Filter as pf
from pgn_filter_dc import PGN_Filter_DC as pfo

new_filter_obj1 = pfo(eco_from = "A57", eco_to = "A59", move_pattern = r"4\.\.\. *a6.*5\. *e3")
new_filter_obj2 = pfo(eco_from = "A57", eco_to = "A59", move_pattern = "")
for i in range(250,315):
    new_filter = pf("/Volumes/Data/DataLake/chess/filtered/split/commentated_li_"+str(i)+".pgn", "/Volumes/Data/DataLake/chess/filtered/wolga_e3", max_games = 10000000)
    new_filter.register_filter(new_filter_obj1, "commentated_wolga_e3_"+str(i)+".pgn")
    new_filter.register_filter(new_filter_obj2, "commentated_wolga_"+str(i)+".pgn")
    new_filter.filter()
