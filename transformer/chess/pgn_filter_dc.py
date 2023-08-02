from dataclasses import dataclass
import re
import chess.pgn

import logging
logger = logging.getLogger("root")
logging.basicConfig(level=logging.DEBUG)

@dataclass
class PGN_Filter_DC:
    elo: int = 0
    elo_both: bool = True
    commentated: bool = False
    eco_from: str = ""
    eco_to: str = ""
    move_pattern: str = ""

    eco_pattern = r'^([A-E][0-9]{2})?$'
    eval_string = "[%eval "
    min_eval_occ = 10

    def is_valid_regex(self, pattern):
        try:
            re.compile(pattern)
            return True
        except re.error:
            return False

    def __post_init__(self):
        if not re.match(self.eco_pattern, self.eco_from) or not re.match(self.eco_pattern, self.eco_from):
            raise ValueError("Invalid ECO format.")
        if self.elo < 0 or self.elo > 3999:
            raise ValueError("Invalid ELO")
        if not self.is_valid_regex(self.move_pattern):
            raise ValueError("Invalid Move Pattern")
        if self.eco_from != "":
            if self.eco_to != "":
                if self.eco_to < self.eco_from:
                    raise ValueError("From Higher than To")
            else:
                self.eco_to = self.eco_from
        elif self.eco_to != "":
            self.eco_from = self.eco_to
        
    def is_a_match(self, game):
        if self.elo > 0:
            if game.headers.get("WhiteElo") is None:
                w_rating = 0
            else:
                w_rating = int(game.headers["WhiteElo"])
            if game.headers.get("BlackElo") is None:
                b_rating = 0
            else:
                b_rating = int(game.headers["BlackElo"])
            if self.elo_both:
                if w_rating < self.elo or b_rating < self.elo:
                    return False
        if self.commentated or self.move_pattern != "":
            str_game = str(game)
            if self.commentated:
                occ = str_game.count(self.eval_string)
                if occ < self.min_eval_occ:
                    return False
            if self.move_pattern != "":
                match = re.search(self.move_pattern, str_game)
                if not match:
                    return False
        if self.eco_from != "":
            eco_code = game.headers.get("ECO", "")
            if eco_code == "":
                return False
            if self.eco_from > eco_code or self.eco_to < eco_code:
                return False
        return True
