import random\
\
"""This program plays a game of Rock, Paper, Scissors between two Players,\
and reports both Player's scores each round."""\
\
moves = ['rock', 'paper', 'scissors']\
\
"""The Player class is the parent class for all of the Players\
in this game"""\
\
\
class Player:\
    def move(self):\
        return 'rock'\
\
    def learn(self, my_move, their_move):\
        pass\
\
\
class RandomPlayer(Player):\
    def move(self):\
        return random.choice(moves)\
\
\
class HumanPlayer(Player):\
    def move(self):\
        while True:\
            Hand = input("Choose Rock, Paper or Scissors\\n\\n").lower()\
            if Hand in moves:\
                return Hand\
            print(f'Sorry, the option "\{Hand\}" is invalid. Try again!')\
\
\
class ReflectPlayer(Player):\
    def __init__(self):\
        self.round = 1\
\
    def move(self):\
        if self.round == 1:\
            self.round += 1\
            return random.choice(moves)\
\
        else:\
            return self.nextmove\
\
    def learn(self, my_move, their_move):\
        self.nextmove = their_move\
\
\
class CyclePlayer(Player):\
    def __init__(self):\
        self.round = 0\
\
    def move(self):\
        while self.round < 3:\
            i = self.round\
            self.round += 1\
            return moves[i]\
\
    def learn(self, my_move, their_move):\
        pass\
\
\
def beats(one, two):\
    if one == two:\
        return\
    else:\
        return ((one == 'rock' and two == 'scissors') or\
                (one == 'scissors' and two == 'paper') or\
                (one == 'paper' and two == 'rock'))\
\
\
class Game:\
    def __init__(self, p1, p2):\
        self.p1 = p1\
        self.p2 = p2\
        self.score1 = 0\
        self.score2 = 0\
\
    def play_round(self):\
        move1 = self.p1.move()\
        move2 = self.p2.move()\
        print(f"\\nPlayer 1: \{move1\}  Player 2: \{move2\}")\
        self.p1.learn(move1, move2)\
        self.p2.learn(move2, move1)\
        result = beats(move1, move2)\
        if result:\
            self.score1 += 1\
        elif result is False:\
            self.score2 += 1\
        else:\
            pass\
\
        print(f"\\nPlayer 1 Score: \{self.score1\}  Player " +\
              f" 2 Score: \{self.score2\}\\n")\
\
    def test(self, score1, score2):\
        if score1 > score2:\
            print("PLAYER 1 WINS!\\n")\
        elif score2 > score1:\
            print("PLAYER 2 WINS!\\n")\
        else:\
            print("YOU TIED!\\n")\
\
    def play_game(self):\
        print("Game start!\\n")\
        for round in range(3):\
            print(f"Round \{round\}:\\n")\
            self.round_counter = round\
            self.play_round()\
        game.test(self.score1, self.score2)\
        print("Game over!")\
\
    def play_singlegame(self):\
        print("Game start!\\n")\
        self.play_round()\
        game.test(self.score1, self.score2)\
        print("Game over!")\
\
\
if __name__ == '__main__':\
    game = Game(HumanPlayer(), RandomPlayer())\
    game.play_game()\
}
