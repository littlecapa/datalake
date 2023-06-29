import chess.pgn
import os

import logging
logger = logging.getLogger("root")
logging.basicConfig(level=logging.DEBUG)

class PGN_Filter():

    def __init__(self, input_file, outputpath, max_games = 100000000, eval_string = "[%eval ", min_evals = 10):
        self.outputpath = outputpath
        self.input_file = input_file
        self.filter_list = []
        self.output_file_names = []
        self.max_games = max_games
        self.eval_string = eval_string
        self.min_evals = min_evals

    def get_valid_filter(self):
        return ["Commentated", "Commentated2000++", "Commentated2000+", "2000++", "2000+"]
    
    def register_filter(self, filter_name, output_filename):
        if filter_name in self.get_valid_filter():
            self.filter_list.append(filter_name)
            self.output_file_names.append(output_filename)
        else:
            logger.error(f"Invalid Filter Name: {filter_name}")

    def create_output_files(self):
        output_files = []
        for file_name in self.output_file_names:
            file_handle = open(os.path.join(self.outputpath, file_name), "w")
            output_files.append(file_handle)
        self.output_files = output_files

    def close_output_files(self):
        for file in self.output_files:
            file.close()
        self.output_files = []
    
    def filter_game(self, game):
        logger.debug(f"Game {game.headers['White']} {game.headers['Black']}")
        valid_filter = []
        if game.headers.get("WhiteElo") is None:
            w_rating = 0
        else:
            w_rating = int(game.headers["WhiteElo"])
        if game.headers.get("BlackElo") is None:
            b_rating = 0
        else:
            b_rating = int(game.headers["BlackElo"])

        if w_rating > 2000 and b_rating > 2000:
            valid_filter.append("2000+")
            valid_filter.append("2000++")
        elif w_rating > 2000 or b_rating > 2000:
            valid_filter.append("2000+")
        
        str_game = str(game)
        occ = str_game.count(self.eval_string)
        logger.debug(f"Occurences {occ}")
        if occ > self.min_evals:
            add_filter = []
            logger.debug(f"Valid Filter: {valid_filter}")
            for filter in valid_filter:
                logger.debug(f"Filter: {filter}")
                add_filter.append("Commentated"+filter)
            valid_filter.extend(add_filter)    
            valid_filter.append("Commentated")
            logger.debug(f"Valid Filter: {valid_filter}")
        logger.debug(f"Valid Filter: {valid_filter}")
        for index, filter in enumerate(self.filter_list):
            if filter in valid_filter:
                logger.debug(f"Index: {index}, Filter: {str(filter)}")
                self.output_files[index].write(str_game + "\n\n")

    def filter(self, clean_up = False):
        if self.filter_list == []:
            logger.error("Empty Filter List")
            return
        
        try:
            self.create_output_files()
            index = 0
            with open(self.input_file) as pgn_file:
                while True:
                    # Read the next game from the input PGN file
                    game = chess.pgn.read_game(pgn_file)
                    if game is None:
                        # End of file
                        break
                    self.filter_game(game)
                    index += 1
                    if index >= self.max_games:
                        break
        except Exception as e:
            logger.error(str(e))
        finally:
            # Close the PGN files
            pgn_file.close()
            self.close_output_files
        

    