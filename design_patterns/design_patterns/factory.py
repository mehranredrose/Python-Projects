from abc import ABC, abstractmethod
from random import choice


class Factory:
    """
    aka Virtual Constructor
    Factory Method is a creational design pattern that
    provides an interface for creating objects in a superclass,
    but allows subclasses to
    alter the type of objects that will be created.
    """

    """
    example is a game like Rock,Paper,Scissor that can be
    played with system or with another player.
    """
    pass


class PlayerBase(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    def move(self):
        m = input('choose your next move ...')
        return m
    # and more ....


class SystemPlayer(PlayerBase):
    def move(self):
        return choice(self.choices)
    # and more ....


class Game:  # this is the Factory design pattern

    @staticmethod
    def start_game():
        game_type = input(
            "Choose Game Type ('s' for single and 'm' for multiple player): ")
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer()
        elif game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print('Invalid Input')
            p1 = None
            p2 = None
        return p1, p2


if __name__ == '__main__':
    player_1, player_2 = Game.start_game()

    for player in [player_1, player_2]:
        player.move()
