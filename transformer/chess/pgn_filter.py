import os
import chess.pgn
import logging
logger = logging.getLogger("root")
logging.basicConfig(level=logging.DEBUG)

class PGN_Filter():

    def __init__(self, input_file, outputpath, max_games = 100000000):
        self.outputpath = outputpath
        self.input_file = input_file
        self.filter_obj_list = []
        self.output_file_names = []
        self.max_games = max_games
    
    def register_filter(self, filter_obj, output_filename):
        self.filter_obj_list.append(filter_obj)
        self.output_file_names.append(output_filename)

    def create_output_files(self):
        output_files = []
        for file_name in self.output_file_names:
            file_handle = open(os.path.join(self.outputpath, file_name), "w")
            output_files.append(file_handle)
            logger.debug(f"Outputfile {file_name} in {self.outputpath} created")
        self.output_files = output_files

    def close_output_files(self):
        for file in self.output_files:
            file.close()
        self.output_files = []
    
    def filter_game(self, game):
        for index, filter_obj in enumerate(self.filter_obj_list):
            if filter_obj.is_a_match(game):
                #logger.debug(f"Index: {index}, Filter: {str(filter)}")
                #logger.debug(f"Write File: {index}")
                self.output_files[index].write(str(game) + "\n\n")

    def filter(self):
        if self.filter_obj_list == []:
            logger.error("Empty Filter List")
            return
        
        try:
            self.create_output_files()
            index = 0
            logger.debug(f"Input File: {self.input_file}")
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
                    #logger.debug(f"File/Index: {self.input_file}, {index}")
        except Exception as e:
            logger.error(str(e))
        finally:
            # Close the PGN files
            pgn_file.close()
            self.close_output_files()
            logger.debug("All Files closed")
        

    