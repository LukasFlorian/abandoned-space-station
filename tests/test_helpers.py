"""
Test module for the helpers module
"""

import unittest
from unittest.mock import patch
import time
import os
import sys

this_path = os.path.dirname(__file__)
this_path = os.path.join(this_path, '..')
os.environ['PYTHONPATH'] = this_path
sys.path.append(os.environ['PYTHONPATH'])

# Import the functions to test
from source.helpers import clear, wait

class TestHelpers(unittest.TestCase):
    """Unittest TestCase class for the helpers module"""
    @patch("os.system")
    def test_clear(self, mock_system):
        """Test that the clear function calls the correct system command."""
        clear()
        # Check if os.system was called with the correct command
        if os.name == 'nt':
            mock_system.assert_called_with('cls')
        else:
            mock_system.assert_called_with('clear')

    def test_wait(self):
        """Test that the wait function waits approximately the correct amount of time."""
        start_time = time.time()
        wait(2)  # Wait for 2 seconds
        end_time = time.time()

        # Check if the elapsed time is approximately 2 seconds
        elapsed_time = end_time - start_time
        self.assertAlmostEqual(elapsed_time, 2, delta=0.5)  # Allow a 0.5 second tolerance

# Run the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestHelpers))
