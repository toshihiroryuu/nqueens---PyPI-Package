import sys
import subprocess
import ast
from collections import namedtuple


# Route n-queens based on algorithm selected.
def queens(n = 4, algo = "divide"):

    print("n-queens",n)

    if algo == "divide":
        # get no of solution possible and their position as list
        count, pos = nqueens_branch(n)
    else:
        # get no of solution possible and their position as list
        count, pos = nqueens_backtrack(n)


# Use Branch and bound to solve the problem.
def nqueens_branch(n):
    # Set initial count to 0
    count = 0
    pos = []
    return count, pos


# Use Backtracking to solve the problem.
def nqueens_backtrack(n):
    count = 0
    # ist to hold queen positions
    pos = []
    return count, pos

# Print the possible soultions as 0,1 on board
def show():
    pass


# Display the solution as an image
def display():
    pass


# save the n quuens image
def save(image_stream, name):
    pass


# Get an image and identify the n-value and position of queens if present.
def scan_queen(image_name):
    count = 0
    pos = []
    return count, pos

# Solve nqueens if queens are present at a position.
def position_solver(n, pos):
    count = 0
    pos = []
    return count, pos


# Solve n-queens for an image
def image_solver():
    if pos.is_empty():
        nqueens_backtrack(n)
    else:
        position_solver(n, pos)
    pass

# Return Positions and solution space as audio.
def alexa():
    pass

queens(4, )