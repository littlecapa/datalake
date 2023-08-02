import os
import chess.pgn
import logging
import re
logger = logging.getLogger("root")
logging.basicConfig(level=logging.DEBUG)
import sys
sys.path.append('/Users/littlecapa/GIT/python/ai_chess_engine/src/libs')
sys.path.append('/Users/littlecapa/GIT/python/ai_chess_engine/src/')
sys.path.append('/Users/littlecapa/GIT/python/ai_chess_engine/')
from chess_nn import Chess_NN as cnn
import numpy as nn

class PGN_Eval_Extractor():

    NO_EVAL = 9999.9999
    NO_MATE = -1 * NO_EVAL

    chess_lib = cnn()

    def __init__(self, input_file, outputpath, csv_seperator = ";", max_games = 100000000):
        self.outputpath = outputpath
        self.input_file = input_file
        input_file_name = os.path.basename(input_file)
        self.output_file = input_file_name.replace(".pgn", ".csv")
        self.max_games = max_games
        self.csv_seperator = csv_seperator
    
    def create_output_file(self):
        logger.debug(f"Outputfile: {os.path.join(self.outputpath, self.output_file)}")
        self.output_file_handle = open(os.path.join(self.outputpath, self.output_file), "w")
    
    def close_output_file(self):
        self.output_file_handle.close()
        
    def write_move_eval(self, int_array_tensor, eval, mate):
        if eval != self.NO_EVAL:
            eval_str = str(eval)
        else:
            eval_str = ""
        if mate != self.NO_MATE:
            mate_str = str(mate)
        else:
            mate_str= ""
        self.output_file_handle.write(f"{int_array_tensor}{eval_str}{self.csv_seperator}{mate_str}\n")

    def get_mate_in(self, comment):
        pattern = r"eval #(-?\d+)"
        match = re.search(pattern, comment)
        if match:
            mate_in = int(match.group(1))
            return mate_in
        else:
            return self.NO_MATE

    def get_evals(self, comment):
        match = re.search(r"\[%eval ([-+]?\d+(\.\d+)?)\]", comment)
        if match:
            return match.group(1), self.NO_MATE
        else:
            return self.NO_EVAL, self.get_mate_in(comment)
    
    def extract_moves(self, node):
        if node.move is not None:
            if node.comment is not None:
                int_values = self.chess_lib.board_to_tensor(board = node.board()).numpy()
                str_tensor = ""
                for value in int_values:
                    str_tensor += str(value) + self.csv_seperator
                eval, mate = self.get_evals(node.comment)
                self.write_move_eval(str_tensor, eval, mate)
        for variation in node.variations:
            self.extract_moves(variation)
                
    def extract(self):
        try:
            self.create_output_file()
            index = 0
            logger.debug(f"Input File: {self.input_file}")
            with open(self.input_file) as pgn_file:
                while True:
                    # Read the next game from the input PGN file
                    game = chess.pgn.read_game(pgn_file)
                    if game is None:
                        # End of file
                        break
                    #logger.debug(f"Game: {game}")
                    self.extract_moves(game)
                    index += 1
                    if index >= self.max_games:
                        break
                    #logger.debug(f"File/Index: {self.input_file}, {index}")
        except Exception as e:
            logger.error(str(e))
        finally:
            # Close the PGN files
            pgn_file.close()
            self.close_output_file()
            logger.debug("All Files closed")
        

    