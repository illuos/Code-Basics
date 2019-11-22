# Coding Basics
# Recursion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Prints out the factorial of a given number
def factorial(n):
    # n = Nonnegative integer input value
    
    if n == 0: # Base case
        return 1
    # Simplified by 
    return n * factorial(n-1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# https://www.mathsisfun.com/games/towerofhanoi.html
# Prints out the steps to solve the Towers of Hanoi game
def towersOfHanoi(n, start = "T1", end = "T3", via = "T2"):
    # n = Number of discs
    # start = The originating position
    # end = The position we aim to move discs to
    # via = The intermediary position we may use temporarily
    
    def move(start, end):
        print(f"Move a disc from {start} to {end}.")

    # If there are 0 discs, we can short circuit and do nothing
    if n == 0:
        return
    # Problem is simplified by moving n-1 discs to intermediary position
    towersOfHanoi(n-1, start, via, end)
    #  Then moving the bottom disc to the final position
    move(start, end)
    #  Then moving the n-1 discs along to the final position
    towersOfHanoi(n-1, via, end, start)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# https://en.wikipedia.org/wiki/Ackermann_function
# Computes the specific value of the Ackermann function of two variables
# NOTE: This is a non-primitive recursive function; It does NOT have a
#  non-recursive solution
def ackermann(m, n):
    # m, n = Two nonnegative integer values given into the function

    if m == 0:      # Case 1: m = 0
        return n+1
    elif n == 0:    # Case 2: m > 0, n = 0
        return ackermann(m-1, 1)
    else:           # Case 3: m > 0, n > 0
        return ackermann(m-1, ackermann(m, n-1))
