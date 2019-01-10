import random

moves = ['rock', 'paper', 'scissors']

class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

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
        self.move_temp = "rock"

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move

class CyclerPlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move

class Game:

    player1 = 0
    player2 = 0
    draw = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        #Player.learn(move1, move2)
        move = self.beats(move1, move2)
        #print(move)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while True:
            try:
                game_count = int(input("How many times do you want to play? :- "))
            except ValueError:
                print("Sorry that does not make sense. Please stick to positive integers - example: 1, 3, 5, 7, etc")
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

    def beats(self, one, two):
        if one == two:
            result = "**Thats a tie**"
            print(result)
            self.scoreboard(result)
        elif ((one == 'rock' and two == 'scissors') or (one == 'scissors' and two == 'paper') or (one == 'paper' and two == 'rock')):
            result = "**Player 1 Win**"
            print(result)
            self.scoreboard(result)
        else:
            result = "**Player 2 Win**"
            print(result)
            self.scoreboard(result)

    def scoreboard(self, result):
        if result == "**Player 1 Win**":
            self.player1 += 1
        elif result == "**Player 2 Win**":
            self.player2 += 1
        else:
            self.draw += 1

        print(f"\n:::Total score::: \n No of draws {self.draw} \n Player 1 total wins {self.player1} \n Player 2 total wins {self.player2}")

if __name__ == '__main__':
    while True:
        try:
            game_play = int(input("Welcome to the game of rock paper scissors. Enter the option (1 or 2 or 3 or 4) you want to play against \n 1. play against a random bot? \n 2. play against a reflect bot? \n 3. play against a cycler bot? \n 4. watch bots play against each other? \n :-"))
            if game_play == 1:
                game = Game(HumanPlayer(), RandomPlayer())
                game.play_game()
            elif game_play == 2:
                game = Game(HumanPlayer(), ReflectPlayer())
                game.play_game()
            elif game_play ==3:
                game = Game(HumanPlayer(), CyclerPlayer())
                game.play_game()
            elif game_play ==4:
                game = Game(RandomPlayer(), ReflectPlayer())
                game.play_game()
            break
        except ValueError:
            print("Does not make sense")
            continue
        if game_play != 1 or game_play != 2 or game_play != 3 or game_play != 4:
            print("Does not make sense")
            continue
