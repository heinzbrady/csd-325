#Brady Heinz 12/19/25 11.2 Assignment


def print_numbers_recursive(n, current=1):
    """
    Recursive Function Approach:
    -----------------------------
    This function uses recursion to print numbers from 1 to n.

    How it works:
    - The function prints the current number.
    - It then calls itself with the next number.
    - The recursion continues until current exceeds n.
    - The base case stops the recursion when current > n.

    Parameters:
    n (int): The upper limit number.
    current (int): The current number being printed (default is 1).
    """
    if current > n:  # Base case
        return
    print(current)
    print_numbers_recursive(n, current + 1)


def print_numbers_iterative(n):
    """
    Non-Recursive (Iterative) Function Approach:
    --------------------------------------------
    This function uses a loop instead of recursion.

    How it works:
    - A for-loop starts at 1 and increments up to n.
    - Each number is printed during the loop.
    - This avoids function call overhead and recursion depth limits.

    Parameters:
    n (int): The upper limit number.
    """
    for i in range(1, n + 1):
        print(i)


def get_valid_input():
    """
    Input Validation:
    -----------------
    Prompts the user until a valid positive integer (> 0) is entered.
    Prevents negative numbers and zero from being used.
    """
    while True:
        try:
            n = int(input("Enter a positive integer greater than 0: "))
            if n > 0:
                return n
            else:
                print("Error: Value must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer.")


# -------------------- Test Code --------------------

n = get_valid_input()

print("\n--- Starting Recursive Function ---")
print_numbers_recursive(n)
print("--- Ending Recursive Function ---\n")

print("--- Starting Non-Recursive Function ---")
print_numbers_iterative(n)
print("--- Ending Non-Recursive Function ---")
