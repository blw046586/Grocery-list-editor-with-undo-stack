# InsertAtCommand.py
from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, target_list, index, item):
        """
        Initializes the command with the target list, the index where
        the item was originally removed from, and the item itself.
        """
        self.target_list = target_list
        self.index = index
        self.item = item

    def execute(self):
        """
        Executes the insert operation to undo a previous removal.
        Inserts the stored 'item' back into the 'target_list' at the
        stored 'index'. Includes validation for the insertion index.
        """
        # Check if the index is valid for insertion (0 up to and including list length)
        # This prevents an error if the list has changed size unexpectedly.
        if 0 <= self.index <= len(self.target_list):
             # Use the list's insert() method
             self.target_list.insert(self.index, self.item)
        # If the index becomes invalid, the command effectively does nothing,
        # preventing a potential crash. Consider if error logging/handling
        # would be appropriate in a more complex application.