# RemoveLastCommand.py
from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, target_list):
        """
        Initializes the command with the list it needs to modify.
        'target_list' is expected to be the list_items from the GroceryList.
        """
        self.target_list = target_list

    def execute(self):
        """
        Removes the last element from the target list.
        This effectively undoes an 'add' operation, which appends to the list.
        Includes a check to ensure the list is not empty before popping.
        """
        # Check if the list has elements before trying to remove one
        if self.target_list:
            # Removes the last item from the list
            self.target_list.pop()
        # If the list is empty, this command does nothing, preventing an error.