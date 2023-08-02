import logging
from torch.utils.data import Dataset
import chess
from bb_loader import BB_Data_Loader

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

class BB_Data_Loader_KKRR(BB_Data_Loader):

    counter = 0

    def __init__(self, data_path):
        super().__init__(data_path)
        self.counter = 0

    def filter_item(self,boards, labels, mates):
        index = 0
        if self.counter == 0:
            logging.info(f"Filter Board: {boards}")
            self.counter += 1
        count = 0
        for color, _ in COLORS.items():
            for piece, piece_name in PIECES.items():
                if piece not in [chess.ROOK, chess.KING]:
                    if boards[index] != 0:
                        return False
                    else:
                        count += 1
                        if count > 2:
                            logging.info(f"Filter Board: {boards}, Count: {count}")
                index += 1
        return True        