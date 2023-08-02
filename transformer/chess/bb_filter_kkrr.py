import os
import logging
from bb_loader_kkrr import BB_Data_Loader_KKRR
import torch

class BB_Filter_KKRR():

    def __init__(self, input_file, outputpath, max_games = 100000000):        
        self.loader = BB_Data_Loader_KKRR(input_file)
        self.file_name = os.path.basename(input_file)
        self.output_filename = os.path.join(outputpath, self.file_name)
        self.max_games = max_games
        self.create_output_file()
    
    def create_output_file(self):
        self.output_file = open(self.output_filename, "w")

    def close_output_files(self):
        self.output_file.flush()
        self.output_file.close()

    def filter(self):
        index = 0
        data_iterator = torch.utils.data.DataLoader(self.loader, batch_size=1, shuffle=False)
        for item in data_iterator:
            line = item[0]
            logging.info(f"Line: {line}")
            if line != "":
                self.output_file.write(line + '\n')
            index += 1
            if index > self.max_games:
                logging.info(f"Index: {index}")
                break
        self.close_output_files()
        logging.debug("All Files closed")
        

    