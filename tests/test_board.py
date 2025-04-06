"""Module with unittests for the Board class."""
import unittest

import os
import sys

this_path = os.path.dirname(__file__)
this_path = os.path.join(this_path, '..')
os.environ['PYTHONPATH'] = this_path
sys.path.append(os.environ['PYTHONPATH'])


from source.board import Board

class TestBoard(unittest.TestCase):
    """Class with unittests for the Board class."""
    def test_board_initialization(self):
        """Test a specific initialization of the Board class."""
        board = Board(5, 5)
        self.assertEqual(board.width, 5)
        self.assertEqual(board.height, 5)
        self.assertEqual(len(board._traps), 5)
        self.assertEqual(len(board._traps[0]), 5)
        self.assertEqual(len(board._surrounding), 5)
        self.assertEqual(len(board._discovered), 5)

    def test_board_random_initialization(self):
        """Test the random initialization of the Board class."""
        board = Board()
        self.assertGreaterEqual(board.width, 5)
        self.assertLessEqual(board.width, 10)
        self.assertGreaterEqual(board.height, 5)
        self.assertLessEqual(board.height, 10)

    def test_board_str_representation(self):
        """Test the string representation of the Board class."""
        board = Board(3, 3)
        board_str = str(board)
        self.assertIn("0 | ? | ? | ? |", board_str)
        self.assertIn("1 | ? | ? | ? |", board_str)
        self.assertIn("2 | ? | ? | ? |", board_str)

    def test_board_solution_representation(self):
        """Test the solution in string representation of the Board class."""
        board = Board(5, 5)
        solution = board.solution
        self.assertIn("0 |", solution)
        self.assertIn("X |", solution)  # Traps are represented as 'X'
        self.assertIn("1 |", solution)  # Numbers represent surrounding traps

    def test_scan_field_safe(self):
        """Test scanning a safe field."""
        board = Board(3, 3)
        board._traps = [[False] * 3 for _ in range(3)]  # No traps
        result = board.scan_field(1, 1)
        self.assertTrue(result)
        self.assertTrue(board._discovered[1][1])

    def test_scan_field_trap(self):
        """Test scanning a field with a trap."""
        board = Board(3, 3)
        board._traps[1][1] = True  # Place a trap
        result = board.scan_field(1, 1)
        self.assertFalse(result)
        self.assertTrue(board._discovered[1][1])

    def test_scan_field_reveal_surrounding(self):
        """Test scanning a field and revealing surrounding fields."""
        board = Board(3, 3)
        board._traps = [[False] * 3 for _ in range(3)]  # No traps
        board._surrounding[1][1] = 0  # No surrounding traps
        board.scan_field(1, 1)
        self.assertTrue(all(board._discovered[row][col] for row in range(3) for col in range(3)))

    def test_place_traps(self):
        """Test placing traps on the board."""
        board = Board(3, 3)
        board._traps = [[False] * 3 for _ in range(3)]  # No traps initially
        board._place_traps(2)
        trap_count = sum(sum(row) for row in board._traps)
        self.assertEqual(trap_count, 2)

    def test_discoverable_count(self):
        """Test the discoverable count decrements correctly."""
        board = Board(3, 3)
        initial_discoverable = board.discoverable
        board.scan_field(0, 0)
        self.assertLess(board.discoverable, initial_discoverable)


if __name__ == "__main__":
    unittest.main()
