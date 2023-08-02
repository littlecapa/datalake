import sys
sys.path.append('..')

from pgn_eval_extractor import PGN_Eval_Extractor as pee

for i in range(100,200):
    new_eval_extractor = pee("/Volumes/Data/DataLake/chess/filtered/split/commentated_li_" +str(i) + ".pgn", "/Volumes/Data/DataLake/chess/filtered/eval_mate")
    new_eval_extractor.extract()
