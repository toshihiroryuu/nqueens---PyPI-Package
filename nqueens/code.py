import matplotlib.pyplot as plt


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
def display(queen_data):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    table = ax.table(cellText = queen_data, loc='center')
    table.set_fontsize(14)
    table.scale(1, 5)

    ax.axis('off')
    plt.show()


# save the n queens image
def save(queen_data, img_name = "nqueen_solution"):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    table = ax.table(cellText = queen_data, loc='center')
    table.set_fontsize(14)
    table.scale(1,5)

    ax.axis('off')
    plt.savefig(img_name)

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
def image_solver(image_name):
    count, pos = scan_queen(image_name)

    if pos.is_empty():
        nqueens_backtrack(n)
    else:
        position_solver(n, pos)
    pass

# Return Positions and solution space as audio.
def alexa():
    pass


# Test code
queens(4, )

queen_data=[
    [0,1,0,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,0,1,0]]

display(queen_data)
save(queen_data, "amk")