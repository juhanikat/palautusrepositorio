WIN_LIMIT = 4
DEUCE_LIMIT = 3


class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scoredict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""

        if self.player1_score == 0 and self.player2_score == 0:
            score = "Love-All"

        elif self.player1_score == self.player2_score:
            if self.player1_score >= DEUCE_LIMIT:
                score = "Deuce"
            else:
                score = f"{self.scoredict[self.player1_score]}-All"

        elif self.player1_score >= WIN_LIMIT or self.player2_score >= WIN_LIMIT:
            minus_result = self.player1_score - self.player2_score
            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"

        else:
            score = f"{self.scoredict[self.player1_score]}-{self.scoredict[self.player2_score]}"

        return score
