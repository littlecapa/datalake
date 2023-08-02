import sys
sys.path.append('..')

from pgn_read_eval import Eval_Reader as er

for i in range(10,11):
    new_eval_reader = er("/Volumes/Data/DataLake/chess/filtered/eval/commentated_li_"+str(i)+".csv")
    tensor, label = new_eval_reader.read()

    print (tensor, label)
