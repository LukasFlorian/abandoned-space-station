"""
Main entry point to execute all unittests in the tests directory.
"""

import unittest

if __name__ == "__main__":
    # Discover and run all tests in the current directory
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir=".", pattern="test_*.py")
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
