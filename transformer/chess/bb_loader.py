import logging
from torch.utils.data import Dataset
import chess

COLORS = {
    chess.WHITE: 'white',
    chess.BLACK: 'black'
}

PIECES = {
    chess.PAWN: 'Pawn', 
    chess.KNIGHT: 'Knight', 
    chess.BISHOP: 'Bishop', 
    chess.ROOK: 'Rook', 
    chess.KING: 'King', 
    chess.QUEEN: 'Queen'}

class BB_Data_Loader(Dataset):

    def __init__(self, data_path):
        self.lines = []
        self.load_data(data_path)

    def __len__(self):
        return len(self.lines)
    
    def filter_item(self,boards, labels, mates):
        return True        

    def items2str(self, boards, labels, mates):
        out = ""
        for b in boards:
            out += str(b) + ";"
        out += labels + ";"
        out += mates
        logging.debug(f"Out String: {out}")
        return str(out)
    
    def __getitem__(self, idx):
        return self.lines[idx]

    def load_data(self, data_path):
        logging.info(f"File: {data_path}")
        with open(data_path, 'r') as file:
            lines = file.readlines()
        logging.debug(f"File: {data_path}, Lines: {len(lines)}")
        for line in lines:
            values = line.strip().split(';')
            feature_values_int = [int(value) for value in values[:-2]]
            if self.filter_item(feature_values_int,values[-2],values[-1]):
                self.lines.append(self.items2str(feature_values_int,values[-2],values[-1]))
