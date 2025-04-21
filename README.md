# Grocery-list-editor-with-undo-stack
Step 1: Inspect the UndoCommand base class

The read-only UndoCommand.py file declares the UndoCommand base class. The UndoCommand class represents a command object: an object that stores all needed information to execute an action at a later point in time. For this lab, a command object stores information to undo a grocery list change made by the user.


Step 2: Inspect the incomplete GroceryList class
The GroceryList class is declared in GroceryList.py. Two attributes exist:

list_items: A list of strings for list items.
undo_stack: A list of UndoCommand references for undo commands. The list represents a stack, so only the append() and pop() methods should be used.
Note that the add_with_undo() method is already implemented. The method adds a new item to the list and pushes a new RemoveLastCommand object onto the undo stack.


Step 3: Implement RemoveLastCommand's execute() method
The RemoveLastCommand class derives from UndoCommand and is declared in RemoveLastCommand.py. When a RemoveLastCommand object is executed, the string list's last element is removed. So when the user appends a new item to the grocery list, a RemoveLastCommand is pushed onto the stack of undo commands. Popping and executing the RemoveLastCommand then removes the item most recently added by the user.

RemoveLastCommand's target_list attribute and __init__() method are already declared:

target_list is a reference to a GroceryList object's list of strings.
__init__() takes a string list as an argument and assigns target_list with the list.
Implement RemoveLastCommand's execute() method to remove target_list's last element.


Step 4: Implement GroceryList's execute_undo() method
Implement GroceryList's executeUndo() method to do the following:

Pop an UndoCommand off the undo stack
Execute the popped undo command
File main.py has some test functions. Each constructs a GroceryListTest object from a list of string commands. Test 1 tests code implemented so far: insertion and undo of insertion. Calls to other test methods are commented-out. Run your code and make sure that test 1 passes before proceeding.


Step 5: Implement the SwapCommand class and GroceryList's swap_with_undo() method
Implement the SwapCommand class in SwapCommand.py. Add necessary methods so that the command can undo swapping two items in the grocery list.

Implement GroceryList's swap_with_undo() method. The method swaps list items at the specified indices, then pushes a SwapCommand to undo that swap onto the undo stack.

Uncomment the line in main.py that calls test2(). Run your code and make sure that both test 1 and test 2 pass.


Step 6: Implement the InsertAtCommand class and GroceryList's remove_at_with_undo() method
Implement the InsertAtCommand class in InsertAtCommand.py. Add necessary methods so that the command can undo removing a grocery list item at an arbitrary index.

Implement GroceryList's remove_at_with_undo() method. The method removes the list item at the specified index, then pushes an InsertAtCommand to undo that removal onto the undo stack.

Uncomment the line in main() that calls test3(). Run your code and make sure that all tests pass. The output from main.py does not affect grading, so consider adding more tests to main.py before submitting code.

Submit your code for grading.
