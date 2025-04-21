# SwapCommand.py
from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, target_list, index1, index2):
        """
        Initializes the command with the target list and the indices
        that were involved in the original swap operation.
        Stores the necessary information to perform the undo (which is
        the same swap operation).
        """
        self.target_list = target_list
        self.index1 = index1
        self.index2 = index2

    def execute(self):
        """
        Executes the swap operation again on the target list using the
        stored indices. This effectively undoes the original swap because
        swapping twice restores the original order.
        Includes checks for valid indices.
        """
        # Get the current length of the list at the time of execution
        list_len = len(self.target_list)

        # Check if the stored indices are still valid within the list bounds
        if 0 <= self.index1 < list_len and 0 <= self.index2 < list_len:
            # Perform the swap using tuple assignment (swaps the items again)
            self.target_list[self.index1], self.target_list[self.index2] = \
                self.target_list[self.index2], self.target_list[self.index1]
        # If indices become invalid (e.g., list shrunk), this command
        # effectively does nothing, preventing an error.