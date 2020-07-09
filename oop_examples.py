'''
 Classes to represent games
'''
'''
a funtion that lives inside a class is a method
'''
'''
a variable inside a class is known as a field
'''
'''
a constructor is a special method that has __init__ to give you flexibility in how you want to create your objects
based on your
 template.
'''




from random import random
class Game:
    """
    General representation of an abstract game.
    """
    fun_level = 5

    def __init__(self, rounds=2,  player1="Mathias", player2="Daniel"):
        self.rounds = 2
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        Print game players
        """
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_round(self):
        """
        Increment rounds by 1
        """
        self.rounds += 1

    def winner(self):
        """pick a winner!"""
        return self.player1 if random() > 0.5 else self.player2


game1 = Game()

game2 = Game(player1="Teddy", player2="Terry")

"""
creating a sub-class
"""


class Tic(Game):
    """
    Tictactoe subclass of game
    """

    def __init__(self, rounds=3, player1="Salindas", player2="Remari"):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing TIC TAC TOE with {}'.format(
            self.player1, self.player2))


ttt = Tic()
ttt.rounds
game1.winner()
ttt.winner()
ttt.print_players()
game1.print_players()
