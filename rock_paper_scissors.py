import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    player1 = 0
    player2 = 0
    draw = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def beats(one, two):
        if one == two:
            result = "**Thats a tie**"
            print(result)
            Player.scoreboard(result)
            #return result
        elif ((one == 'rock' and two == 'scissors') or (one == 'scissors' and two == 'paper') or (one == 'paper' and two == 'rock')):
            result = "**Player 1 Win**"
            print(result)
            Player.scoreboard(result)
            #return result
        else:
            result = "**Player 2 Win**"
            print(result)
            Player.scoreboard(result)
            #return result

    def scoreboard(result):
        if result == "**Player 1 Win**":
            Player.player1 += 1

        elif result == "**Player 2 Win**":
            Player.player2 += 1

        else:
            Player.draw += 1

        print(f"\n:::Total score::: \n No of draws {Player.draw} \n Player 1 total wins {Player.player1} \n Player 2 total wins {Player.player2}")

class HumanPlayer(Player):
    def move(self):
        while True:
                user_input = input("Pick one - \"rock\" or \"paper\" or \"scissors\":-  ")
                if user_input != "rock" and user_input != "paper" and user_input != "scissors":
                    print(f"common human you entered {user_input} instead of rock or paper or scissors")
                    continue
                else:
                    break
        return user_input

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    def __init__(self):
        self.move_temp = random.choice(moves)

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move

class Cycler(Player):
    def move(self):
        if my_move == "rock":
            return "paper"
        elif my_move == "paper":
            return "scissors"
        elif my_move == "scissors":
            return "rock"
        else:
            return "rock"

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        #Player.learn(move1, move2)
        move = Player.beats(move1, move2)
        #print(move)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while True:
            try:
                game_count = int(input("How many times do you want to play? :- "))
            except ValueError:
                print("Sorry that does not make sense. Please stick to positive integers - example: 5, 7")
                continue
            if game_count < 0 or game_count == 0:
                print("Please enter a positive integer")
                continue
            else:
                break
        for round in range(game_count):
            print(f"\n*****Round {round}:*****")
            self.play_round()
        print("Game over!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
