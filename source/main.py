"""
Main module, script to execute in order to play
"""

import os
import sys

this_path = os.path.dirname(__file__)
this_path = os.path.join(this_path, '..')
os.environ['PYTHONPATH'] = this_path
sys.path.append(os.environ['PYTHONPATH'])

from source.game import Game

def play() -> None:
    """
    Main function to play the game
    """
    Game()

if __name__ == "__main__":
    play()
