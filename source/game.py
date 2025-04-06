"""
Game module for the abandoned space station game
"""

import os
import sys

this_path = os.path.dirname(__file__)
this_path = os.path.join(this_path, '..')
os.environ['PYTHONPATH'] = this_path
sys.path.append(os.environ['PYTHONPATH'])

from source.board import Board
from source.helpers import clear, wait

class Game:
    """
    A class representing the game, its state and methods to create a user interface based on the board state.
    """
    def __init__(self, wait_time: float = 5):
        """
        Initializes the game with a new board.
        """
        # Initialize the board
        self._board = None

        # Initialize the game state
        # self._game_over = True does not mean the user lost, it means the game is over
        self._game_over = False

        # Initialize the wait time (as an optional attribute so it can be set to zero for testing)
        self._wait_time = wait_time

        # Initialize the main menu
        self.main_menu()

    def main_menu(self):
        """
        Prints the introduction to the game.
        """
        clear()
        # Intro
        print("Welcome to the abandoned space station game!")
        print("You are an astronaut on an abandoned space station.")
        print("Be careful, the station is full of traps and hazards.\n")
        print("Your mission is to find locate all all safe zones on the station, while avoiding the traps.\n")
        print("Unfortunately, your means of communicating with the ground station are limited.")
        print("Your only tool is a scanner that can detect the presence of traps around you.")
        print("However, that means you need to be inside the zone that you want to scan, so you must be careful not to step on any traps.")
        print("If you step on a trap, you will be killed and the game will be over.\n")
        print("Do you want to start the game? (y/n) ")

        valid_action = False
        while not valid_action:
            choice = str(input())
            try:
                choice = choice.lower()
                assert choice in ["y", "n"]
                valid_action = True
                if choice == "y":
                    self.play_menu()
                else:
                    print("Goodbye!")
            except AssertionError:
                print("\nInvalid input. Please enter 'y' or 'n'. ")

    def display_board_and_instructions(self):
        """
        Displays the board of the game and instructions
        """
        clear()
        print("Here is the map of the space station:")
        print(self._board)
        print("Question marks represent cells that you have not scanned yet.")
        print("Numbers represent the number of traps around the cell.\n")
        print("Let's start!")
        print("Enter the row and column of the cell you want to scan (e.g. 1 2): ")

    def play_menu(self):
        """
        Displays the board of the game and handles user interactions.
        """
        self._game_over = False
        self._board = Board()
        while not self._game_over:
            self.display_board_and_instructions()
            valid_action = False
            while not valid_action:
                try:
                    # Read the row and column from the user
                    cell = str(input())
                    row, col = map(int, cell.split())
                    assert 0 <= row < self._board.height and 0 <= col < self._board.width
                    valid_action = True

                    # Scan the field
                    success = self._board.scan_field(row, col)

                    if not success:
                        # Game over
                        self._game_over = True
                        # Clear the screen and print the defeat message
                        clear()
                        print("Oh no, you stepped on a trap! Game over.")
                        print("\nThe solution was:")
                        print(self._board.solution)
                    else:
                        if self._board.discoverable == 0:
                            self._game_over = True
                            # Clear the screen and print the victory message
                            clear()
                            print("Congratulations! You have found all the safe cells!")
                            print("\nThe final solution is:")
                            print(self._board.solution)
                except ValueError:
                    print("Invalid input. Please enter two integer numbers separated by a space.")
                except AssertionError:
                    print("Invalid input. Please enter a valid row and column.")
        print("\nYou'll automatically return to the main menu in 5 seconds.")
        wait(self._wait_time)
        self.main_menu()
