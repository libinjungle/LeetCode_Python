'''
chess game.
use abstract factory pattern to create chess roles
'''
import random

class Chess:

  def __init__(self, chess_factory = None):
    self.chess_factory = chess_factory

  def show_role(self):
    role = self.chess_factory.get_role()
    print "The role here is {}".format(role)


class King:
  def speak(self):
    return 'I am King'

  def __str__(self):
    return "King"

class Queen:
  def speak(self):
    return 'I am Queen'

  def __str__(self):
    return "Queen"

class ChessFactory:
  def get_role(self):
    return random.choice([King, Queen])()


def get_factory():
  # Can not use ChessFactory
  return ChessFactory()


if __name__ == '__main__':
  chess = Chess(get_factory())
  chess.show_role()

