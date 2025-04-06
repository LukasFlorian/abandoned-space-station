"""
Test module for the main script
"""
import unittest
from unittest.mock import patch
import os
import sys

this_path = os.path.dirname(__file__)
this_path = os.path.join(this_path, '..')
os.environ['PYTHONPATH'] = this_path
sys.path.append(os.environ['PYTHONPATH'])


import source
from source.main import play


class TestMain(unittest.TestCase):
    """Test cases for the main module"""

    @patch('source.main.Game')
    def test_play(self, mock_game: unittest.mock.MagicMock) -> None:
        """Test the play function"""
        # Call the play function
        play()

        # Check that Game was instantiated
        mock_game.assert_called_once()

    def test_pythonpath(self) -> None:
        """Test that PYTHONPATH is set correctly"""
        # Import the main module

        # Check that the correct path was appended to sys.path
        expected_path = os.path.dirname(os.path.dirname(os.path.abspath(source.main.__file__)))
        sys_paths = [os.path.abspath(p) for p in sys.path]
        self.assertIn(expected_path, sys_paths)


if __name__ == '__main__':
    unittest.main()
