# main.py
from GroceryList import GroceryList
# Ensure GroceryListTest is imported (assuming it's in GroceryListTest.py)
from GroceryListTest import GroceryListTest

# Test 1 tests insertion and undo of insertion only
def test1(test_feedback):
    test = GroceryListTest([
        "add carrots",
        "verify carrots",
        "undo",   # undo addition of carrots
        "verify", # verify empty list
        "add potatoes",
        "verify potatoes",
        "add carrots",
        "verify potatoes,carrots",
        "add lettuce",
        "verify potatoes,carrots,lettuce",
        "add rice",
        "verify potatoes,carrots,lettuce,rice",
        "add cilantro",
        "verify potatoes,carrots,lettuce,rice,cilantro",
        "undo",   # undo addition of cilantro
        "verify potatoes,carrots,lettuce,rice",
        "undo",   # undo addition of rice
        "verify potatoes,carrots,lettuce",
        "undo",   # undo addition of lettuce
        "verify potatoes,carrots",
        "undo",   # undo addition of carrots
        "verify potatoes",
        "undo",   # undo addition of potatoes
        "verify",
        "add basil",
        "verify basil",
        "add onions",
        "verify basil,onions",
        "add spinach",
        "verify basil,onions,spinach",
        "undo",   # undo addition of spinach
        "verify basil,onions",
        "undo",   # undo addition of onions
        "verify basil",
        "undo",   # undo addition of basil
        "verify"
    ], test_feedback)
    return test.execute()

# Test 2 tests insertion and swapping and the undo of each
def test2(test_feedback):
    test = GroceryListTest([
        "add chips",
        "add cookies",
        "add waffles",
        "add syrup",
        "add ice cream",
        "add lettuce",
        "verify chips,cookies,waffles,syrup,ice cream,lettuce",
        "swap 1 4", # swap cookies and ice cream
        "verify chips,ice cream,waffles,syrup,cookies,lettuce",
        "undo", # undo the swap
        "verify chips,cookies,waffles,syrup,ice cream,lettuce"
    ], test_feedback)
    return test.execute()

# Test 3 tests all commands
def test3(test_feedback):
    test = GroceryListTest([
        "add orange juice",
        "add apple juice",
        "verify orange juice,apple juice",
        "undo", # undo add apple juice
        "verify orange juice",
        "removeat 0", # Use 'removeat' as defined in GroceryListTest
        "verify",
        "undo", # undo remove orange juice
        "verify orange juice",
        "undo", # undo add orange juice
        "verify",
        "add mango juice",
        "verify mango juice",
        "add grapefruit juice",
        "add grape juice",
        "verify mango juice,grapefruit juice,grape juice",
        "swap 0 1",
        "verify grapefruit juice,mango juice,grape juice",
        "add strawberry smoothie",
        "verify grapefruit juice,mango juice,grape juice,strawberry smoothie",
        "swap 2 3",
        "verify grapefruit juice,mango juice,strawberry smoothie,grape juice",
        "removeat 3",
        "verify grapefruit juice,mango juice,strawberry smoothie",
        "removeat 1",
        "verify grapefruit juice,strawberry smoothie",
        "swap 0 1",
        "verify strawberry smoothie,grapefruit juice",
        "undo", # undo swap 0 1
        "undo", # undo removal of mango juice (at index 1) -> inserts mango juice at 1
        "undo", # undo removal of grape juice (at index 3) -> inserts grape juice at 3
        "undo", # undo swap 2 3
        "undo", # undo add strawberry smoothie
        "verify grapefruit juice,mango juice,grape juice", # State before add strawberry smoothie
        "undo", # undo swap 0 1
        "undo", # undo add grape juice
        "verify mango juice,grapefruit juice", # State before add grape juice
        "undo", # undo add grapefruit juice
        "verify mango juice", # State before add grapefruit juice
        "undo", # undo add mango juice
        "verify" # Should be empty
    ], test_feedback)
    return test.execute()

# FeedbackPrinter is used to print feedback when testing locally
# (Or when running in environments that capture stdout)
class FeedbackPrinter:
    def write(self, text):
        print(text)

# --- Main program execution ---
if __name__ == "__main__":
    feedback = FeedbackPrinter()
    tests_passed = [] # Use a list to store results

    print("--- Running Test 1 ---")
    tests_passed.append(test1(feedback))
    print("-" * 20) # Separator

    # --- Uncomment the following lines as you complete steps 5 and 6 ---
    print("\n--- Running Test 2 ---")
    tests_passed.append(test2(feedback))
    print("-" * 20) # Separator

    print("\n--- Running Test 3 ---")
    tests_passed.append(test3(feedback))
    print("-" * 20) # Separator
    # --- End uncomment section ---

    # Print summary
    print("\n--- Test Summary ---")
    all_passed = True
    for i in range(len(tests_passed)):
        result = "PASS" if tests_passed[i] else "FAIL"
        print(f'Test {i + 1}: {result}')
        if not tests_passed[i]:
            all_passed = False
    print("------------------")
    if all_passed:
        print("All executed tests passed!")
    else:
        print("Some tests failed.")
    print("------------------")