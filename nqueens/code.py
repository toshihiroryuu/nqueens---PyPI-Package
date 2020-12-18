import matplotlib.pyplot as plt


# Route n-queens based on algorithm selected.
def queens(n = 4, algo = "branch"):

    print("n-queens",n)

    if algo == "branch":
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
    try:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        table = ax.table(cellText = queen_data, loc='center')
        table.set_fontsize(14)
        table.scale(1, 5)

        ax.axis('off')
        plt.show()
    except Exception as ex:
        print(ex)


# save the n queens image
def save(queen_data, img_name = "nqueen_solution"):
    try:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        table = ax.table(cellText = queen_data, loc='center')
        table.set_fontsize(14)
        table.scale(1,5)

        ax.axis('off')
        plt.savefig(img_name)
    except Exception as ex:
        print(ex)

# Get an image and identify the n-value, no of queens and position of queens if present.
def scan_queen(image_name):
    n = 0
    count = 0
    pos = []

    return count, pos, n

# Solve nqueens if queens are present at a position.
def position_solver(n, pos):
    count = 0
    pos = []
    return count, pos


# Solve n-queens for an image
def image_solver(image_name):
    try:
        count, pos, n = scan_queen(image_name)

        if pos.is_empty():
            nqueens_backtrack(n)
        else:
            position_solver(n, pos)
    except Exception as ex:
        print(ex)

# Return Positions and solution space as audio.
def alexa():
    pass
