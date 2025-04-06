"""
Test module for the game class
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock


import os
import sys

this_path = os.path.dirname(__file__)
this_path = os.path.join(this_path, '..')
os.environ['PYTHONPATH'] = this_path
sys.path.append(os.environ['PYTHONPATH'])


from source.game import Game


class TestGame(unittest.TestCase):
    """Test cases for the Game class"""


    @patch('builtins.input')
    def test_main_menu_play(self, mock_input: MagicMock) -> None:
        """Test the main menu when selecting to play"""
        # Mock input to return 'y' (play)
        mock_input.return_value = 'y'

        # Mock play_menu to avoid actual gameplay
        with patch.object(Game, 'play_menu') as mock_play_menu:
            Game(wait_time = 0)
            mock_play_menu.assert_called_once()

    @patch('builtins.input')
    def test_main_menu_quit(self, mock_input: unittest.mock.MagicMock) -> None:
        """Test the main menu when selecting to quit"""
        # Mock input to return 'n' (quit)
        mock_input.return_value = 'n'

        # Create a game instance and check it doesn't raise exceptions
        try:
            Game(wait_time = 0)
            # It should reach here without calling play_menu
        except (ValueError, TypeError) as e:
            self.fail(f"Game(wait_time = 0) raised exception unexpectedly: {e}")

    @patch('builtins.input')
    def test_main_menu_invalid_then_valid(self, mock_input: unittest.mock.MagicMock) -> None:
        """Test the main menu with invalid input followed by valid input"""
        # Mock input to return invalid input, then 'n' (quit)
        mock_input.side_effect = ['invalid', 'n']

        # Create a game instance
        Game(wait_time = 0)

        # Check that input was called twice
        self.assertEqual(mock_input.call_count, 2)

    @patch('source.game.clear')
    def test_display_board_and_instructions(self, mock_clear: unittest.mock.MagicMock) -> None:
        """Test displaying the board and instructions"""
        # Create a game instance with a mocked board
        with patch.object(Game, 'main_menu'):
            game = Game(wait_time = 0)

            # Call the method
            game.display_board_and_instructions()

            # Check that clear was called
            mock_clear.assert_called_once()


    @patch('source.game.wait')
    @patch('builtins.input')
    def test_play_menu_trap(self, mock_input: unittest.mock.MagicMock, mock_wait: unittest.mock.MagicMock) -> None:
        """Test playing the game and hitting a trap"""
        # Create a game instance
        with patch('source.game.Board') as mock_board_class:
            # Mock the board instance
            mock_board = MagicMock()
            mock_board_class.return_value = mock_board

            # Set up the board properties
            mock_board.height = 5
            mock_board.width = 5

            # First scan will hit a trap
            mock_board.scan_field.return_value = False

            # Mock input to return coordinates
            mock_input.return_value = '2 3'

            # Create game and handle main menu patching
            with patch.object(Game, 'main_menu'):
                game = Game(wait_time = 0)
                # Replace the mocked board created during Game initialization
                game._board = mock_board
                game._game_over = False

                # Call play_menu
                game.play_menu()

                # Check that scan_field was called with the right coordinates
                mock_board.scan_field.assert_called_with(2, 3)

                # Check that wait was called
                mock_wait.assert_called()

    @patch('builtins.input')
    def test_play_menu_win(self, mock_input: unittest.mock.MagicMock) -> None:
        """Test playing the game and winning"""
        # Create a game instance
        with patch('source.game.Board') as mock_board_class:
            # Mock the board instance
            mock_board = MagicMock()
            mock_board_class.return_value = mock_board

            # Set up the board properties
            mock_board.height = 5
            mock_board.width = 5

            # Scan will be successful and no more discoverable cells
            mock_board.scan_field.return_value = True

            # This is the key fix - use a property mock for discoverable
            type(mock_board).discoverable = PropertyMock(return_value=0)

            # Mock input to return coordinates
            mock_input.return_value = '2 3'

            # Create game and handle main menu patching
            with patch.object(Game, 'main_menu'):
                game = Game(wait_time = 0)
                # Replace the mocked board created during Game initialization
                game._board = mock_board
                game._game_over = False

                # Call play_menu
                game.play_menu()

                # Check that scan_field was called
                mock_board.scan_field.assert_called()

    @patch('builtins.input')
    def test_play_menu_invalid_input(self, mock_input: unittest.mock.MagicMock) -> None:
        """Test playing the game with invalid input"""
        # Create a game instance
        with patch('source.game.Board') as mock_board_class:
            # Mock the board instance
            mock_board = MagicMock()
            mock_board_class.return_value = mock_board

            # Set up the board properties
            mock_board.height = 5
            mock_board.width = 5

            # Mock input to return invalid coordinates, then valid ones
            mock_input.side_effect = ['invalid', '10 10', '2 3']

            # Scan will be successful
            mock_board.scan_field.return_value = False

            # Create game and handle main menu patching
            with patch.object(Game, 'main_menu'):
                game = Game(wait_time = 0)
                # Replace the mocked board created during Game initialization
                game._board = mock_board
                game._game_over = False

                # Call play_menu
                game.play_menu()

                # Check that input was called multiple times
                self.assertGreaterEqual(mock_input.call_count, 2)


if __name__ == '__main__':
    unittest.main()
