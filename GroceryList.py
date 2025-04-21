# GroceryList.py
# Ensure the command classes are imported correctly
from RemoveLastCommand import RemoveLastCommand
from SwapCommand import SwapCommand
from InsertAtCommand import InsertAtCommand

class GroceryList:
    def __init__(self):
        """
        Initializes an empty grocery list and an empty undo stack.
        """
        self.list_items = []  # List of strings for grocery items
        self.undo_stack = []  # List of UndoCommand references (used as a stack)

    def add_with_undo(self, item):
        """
        Adds an item to the end of the list and pushes a command
        (RemoveLastCommand) onto the undo stack to allow reversal.
        """
        self.list_items.append(item)
        # Create command to undo the add (which is removing the last item)
        command = RemoveLastCommand(self.list_items)
        self.undo_stack.append(command) # Push onto stack

    def swap_with_undo(self, index1, index2):
        """
        Swaps items at the specified indices (if valid) and pushes a command
        (SwapCommand) onto the undo stack to allow reversal.
        """
        list_len = len(self.list_items)
        # Check if indices are valid before attempting swap
        if 0 <= index1 < list_len and 0 <= index2 < list_len and index1 != index2:
            # Perform the swap
            self.list_items[index1], self.list_items[index2] = \
                self.list_items[index2], self.list_items[index1]
            # Create command to undo the swap (which is swapping again)
            command = SwapCommand(self.list_items, index1, index2)
            self.undo_stack.append(command) # Push onto stack
        # Note: If indices are invalid or the same, no swap occurs and no undo command is added.

    def remove_at_with_undo(self, index):
        """
        Removes the item at the specified index (if valid) and pushes a command
        (InsertAtCommand) onto the undo stack to allow reversal.
        """
        list_len = len(self.list_items)
        # Check if index is valid before attempting removal
        if 0 <= index < list_len:
            # Store the item being removed *before* removing it to use in the undo command
            removed_item = self.list_items[index]
            # Perform the removal
            self.list_items.pop(index)
            # Create command to undo the removal (which is inserting it back)
            command = InsertAtCommand(self.list_items, index, removed_item)
            self.undo_stack.append(command) # Push onto stack
        # Note: If the index is invalid, no removal occurs and no undo command is added.


    def execute_undo(self):
        """
        If the undo stack is not empty, pops the most recent command
        from the stack and executes its 'execute()' method to reverse
        the last performed action (add, swap, or remove_at).
        """
        if self.undo_stack: # Check if the stack is not empty
            command = self.undo_stack.pop()
            command.execute()

    # --- Methods required by GroceryListTest ---

    def get_undo_stack_length(self):
        """
        Returns the current number of commands on the undo stack.
        Required by GroceryListTest for verification.
        """
        return len(self.undo_stack)

    def get_list_copy(self):
        """
        Returns a shallow copy of the internal list items.
        Required by GroceryListTest's 'verify' command. Returning a copy
        ensures the test class doesn't inadvertently modify the list.
        """
        # Using list() constructor or slicing creates a shallow copy
        return list(self.list_items)
        # Alternative: return self.list_items[:]

    # --- Optional helper methods ---

    def get_list_string(self):
        """ Helper to get comma-separated string representation for testing """
        return ",".join(self.list_items)

    def __str__(self):
        """ Optional: String representation for direct printing of the list """
        return str(self.list_items) # Or use get_list_string()