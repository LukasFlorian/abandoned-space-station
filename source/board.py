"""
Board module for the abandoned space station game
"""

from random import randint


class Board:
    """
    This class represents a board for the game, containing information about the position of traps, the number of surrounding traps and the state of each cell (discovered or not).
    """
    def __init__(self, width: int = randint(5,10), height: int = randint(5,10)):
        """
        Initializes the board based on the width and height parameters.

        Args:
            width (int, optional): Board width (number of columns). Defaults to randint(5,10).
            height (int, optional): Board height (number of rows). Defaults to randint(5,10).
        """
        # board width
        self._width = width

        # board height
        self._height = height

        # String to print the board
        self._separator = "  |" + "---|" * self._width + "\n"

        # Booleans to indicate if there is a trap in a cell
        self._traps = [[False for _ in range(width)] for _ in range(height)]

        # Number of traps surrounding a cell
        self._surrounding = [[0 for _ in range(width)] for _ in range(height)]

        # Booleans to indicate if a cell has been discovered
        self._discovered = [[False for _ in range(width)] for _ in range(height)]

        # Determine random number of traps to place
        num_cells = self._width * self._height
        num_traps = randint(num_cells//10, num_cells//3)

        # Number of cells that can  be discovered safely (no traps)
        self.discoverable = num_cells - num_traps

        # Placing traps on the board
        self._place_traps(num_traps)

    @property
    def width(self):
        """
        Returns the width of the board.
        
        Returns:
            int: board width (number of columns)
        """
        return self._width

    @property
    def height(self):
        """
        Returns the height of the board.
        
        Returns:
            int: board height (number of rows)
        """
        return self._height

    def __str__(self):
        """Returns a string representation of the board.
            
        Returns:
            str: Printable board in string form.
        """
        # Initialize the board string with the column numbers
        printed_board = " " * 4
        for col in range(self.width):
            printed_board += str(col) + " " * 3
        printed_board += "\n" + self._separator

        # Add the rows to the board string
        for row in range(self.height):
            # Add the row number to the board string
            printed_board += str(row) + " | "
            for col in range(self.width):
                if self._discovered[row][col]:
                    # If the cell is discovered, print the number of surrounding traps
                    printed_board += str(self._surrounding[row][col]) + " | "
                else:
                    # If the cell is not discovered, print a question mark
                    printed_board += "? | "
            # Add a separator between rows
            printed_board += "\n"
            printed_board += self._separator
        return printed_board

    def _place_traps(self, num_traps: int = 2):
        """
        Places traps on the board.
        """
        # Place traps randomly on the board
        traps = set()
        while len(traps) < num_traps:
            # Generate random row and column indices for the trap
            row = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            # Add the trap to the set of traps if it is not already in the set (by definition of the set type)
            traps.add((row, col))

        # Update the traps and surrounding attributes of the board
        for row, col in traps:
            # Set the trap boolean at the given row and column index to True
            self._traps[row][col] = True
            # Increment the surrounding attribute of the board for the neighboring cells of the trapped cell
            if row > 0:
                self._surrounding[row - 1][col] += 1
            if row < self.height - 1:
                self._surrounding[row + 1][col] += 1
            if col > 0:
                self._surrounding[row][col - 1] += 1
            if col < self.width - 1:
                self._surrounding[row][col + 1] += 1
            if row > 0 and col > 0:
                self._surrounding[row - 1][col - 1] += 1
            if row > 0 and col < self.width - 1:
                self._surrounding[row - 1][col + 1] += 1
            if row < self.height - 1 and col > 0:
                self._surrounding[row + 1][col - 1] += 1
            if row < self.height - 1 and col < self.width - 1:
                self._surrounding[row + 1][col + 1] += 1

    @property
    def solution(self):
        """
        Returns the solution for the board (all traps and numbers of traps surrounding each field)

        Returns:
            str: String representation of the board solution
        """
        # Initialize the board string with the column numbers
        printed_board = " " * 4
        for col in range(self.width):
            printed_board += str(col) + " " * 3
        printed_board += "\n" + self._separator

        # Print the board with the numbers of traps surrounding each field and the traps themselves
        for row in range(self.height):
            # Print the row number
            printed_board += str(row) + " | "
            for col in range(self.width):
                if self._traps[row][col]:
                    # Print the traps as X's
                    printed_board += "X | "
                else:
                    # Print the numbers of traps surrounding each field if there is not trap in that cell
                    printed_board += str(self._surrounding[row][col]) + " | "
            # Print the separator after each row
            printed_board += "\n"
            printed_board += self._separator
        return printed_board

    def scan_field(self, row: int, col: int) -> bool:
        """
        Scans a field on the board and returns True if the field is safe, False if the field is a trap. If the field is safe, it also reveals all safe fields surrounding the field. If the field is a trap, it reveals the trap.

        Args:
            row (int): row of the field to be scanned
            col (int): column of the field to be scanned

        Returns:
            bool: Boolean indicating whether the field is safe or not
        """
        # Check if the field is a trap; if it is, return False
        if self._traps[row][col]:
            self._discovered[row][col] = True
            self.discoverable -= 1
            return False
        # If the field is not a trap but surrounded by traps, reveal only the selected field
        if self._surrounding[row][col] > 0:
            # Reveal the field
            self._discovered[row][col] = True
            # Decrement the number of discoverable fields
            self.discoverable -= 1
            return True
        # If the field is not a trap and has no surrounding traps, reveal all safe fields surrounding the field
        # Use a queue to keep track of the fields to be revealed
        # Use a set to keep track of the fields that have already been checked to avoid infinite loops
        queue = set()
        checked = set()
        queue.add((row, col))
        while queue:
            # Get the next field to be revealed from the queue
            row, col = queue.pop()

            # Reveal the field
            self._discovered[row][col] = True

            # Decrement the number of discoverable fields
            self.discoverable -= 1

            # Add the field to the set of checked fields
            checked.add((row, col))

            if self._surrounding[row][col] == 0:
                # Add the surrounding fields to the queue if they have not been checked yet

                if row > 0 and (row - 1, col) not in checked:
                    queue.add((row - 1, col))

                if row < self.height - 1 and (row + 1, col) not in checked:
                    queue.add((row + 1, col))

                if col > 0 and (row, col - 1) not in checked:
                    queue.add((row, col - 1))

                if col < self.width - 1 and (row, col + 1) not in checked:
                    queue.add((row, col + 1))

                if row > 0 and col > 0 and (row - 1, col - 1) not in checked:
                    queue.add((row - 1, col - 1))

                if row > 0 and col < self.width - 1 and (row - 1, col + 1) not in checked:
                    queue.add((row - 1, col + 1))

                if row < self.height - 1 and col > 0 and (row + 1, col - 1) not in checked:
                    queue.add((row + 1, col - 1))

                if row < self.height - 1 and col < self.width - 1 and (row + 1, col + 1) not in checked:
                    queue.add((row + 1, col + 1))
        return True
