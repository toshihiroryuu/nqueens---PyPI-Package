import math
import copy
import numpy as np
from gtts import gTTS
from PIL import Image
import matplotlib.pyplot as plt

class Queen:

    def __init__(self, n = 0, algo = "branch", pos = []):
        self.n = n
        self.algo = algo
        self.pos = []

        self.count = 0
        self.queen_data = []

        if n > 0:
            self.router()

    # Route n-queens based on algorithm selected.
    def router(self):

        try:
            if self.algo == "branch":
                # get no of solution possible and their position as list
                self.nqueens_branch()
            else:
                # get no of solution possible and their position as list
                self.nqueens_backtrack()

        except Exception as ex:
            print(ex)

    def pprint(self):
        try:
            print("N = ", self.n)
            print("No of solutions possible = ", self.count)

            print("Solution space = ", self.queen_data)

            if self.count != 0:
                print("Position of Queens = ", self.pos)

        except Exception as ex:
            print(ex)

    def nqueens_backtrack(self):

        try:
            board = []

            for i in range(self.n):
                roww = []
                for j in range(self.n):
                    roww.append(0)
                board.append(roww)

            rowmask = 0
            ldmask = 0
            rdmask = 0
            row = 0

            self.solve_board(board, row, rowmask, ldmask, rdmask)

        except Exception as ex:
            print(ex)

    def solve_board(self, board, row, rowmask,ldmask, rdmask):

        try:
            all_rows_filled = (1 << self.n) - 1

            if (rowmask == all_rows_filled):
                self.count = self.count + 1
                self.queen_data.append(copy.deepcopy(board))

            safe = all_rows_filled & (~(rowmask | ldmask | rdmask))

            while (safe > 0):

                p = safe & (-safe)
                col = (int)(math.log(p)/math.log(2))
                board[row][col] = 1
                self.pos.append([row, col])

                self.solve_board(board, row+1, rowmask|p, (ldmask|p) << 1, (rdmask|p) >> 1)

                safe = safe & (safe-1)

                board[row][col] = 0

        except Exception as ex:
            print(ex)


    def nqueens_branch(self):
        pass

    # Display the solution as an image
    def display(self):

        try :
            rows, cols = len(self.queen_data), len(self.queen_data[0])
            print("No of Solutions ", rows)

            for i in range(rows):
                print("=========================================")
                print("Solution : ", i+1)
                fig = plt.figure()
                ax = fig.add_subplot(1, 1, 1)

                table = ax.table(cellText = self.queen_data[i], loc='center')
                table.set_fontsize(14)
                table.scale(1, 5)

                ax.axis('off')
                plt.show()
                print("=========================================")

        except Exception as ex:
            print(ex)


    # save the n queens image
    def save(self):

        try:
            img_name = "nqueen_solution"

            rows, cols = len(self.queen_data), len(self.queen_data[0])
            print("No of Solutions ", rows)

            for i in range(rows):
                print("Solution : ", i+1, " - Saved as " + img_name + "_" + str(i+1) + ".png")
                fig = plt.figure()
                ax = fig.add_subplot(1, 1, 1)

                table = ax.table(cellText = self.queen_data[i], loc='center')
                table.set_fontsize(14)
                table.scale(1, 5)

                ax.axis('off')

                plt.savefig(img_name + "_" + str(i+1))

        except Exception as ex:
            print(ex)

    # Get an image and identify the n-value, no of queens and position of queens if present.
    def scan_queen(self, image_path):

        try:
            img = Image.open(image_path).convert('RGB')
            pixel = img.load()

            width = img.size[0]
            height = img.size[1]

            white = (255, 255, 255)

            for i in range(width - 1):
                if pixel[i, (height/2)] == white and pixel[i+1, (height/2)] != white:
                    self.n += 1

            self.n = self.n-1

            print("No of Rows identified is ", self.n)

            if self.n > 0:
                self.router()

        except Exception as ex:
            print(ex)

    # Return Positions and solution space as audio.
    def alexa(self, language = "en", speed = "fast", save = True):

        try:
            tt1 = str(self.n)+"Queens Problem "
            tt2 = str(self.count) + "Solutions Possible"


            pos_text = " "
            for i, pair in enumerate(self.pos):
                pos_text = pos_text + "Pair" + str(i+1) + str(pair)

            tt3 = "Queens are present at positions " + pos_text

            textt = tt1 + tt2 + tt3

            bool = False
            if speed == "slow":
                bool = True

            out = gTTS(text = textt, lang = language, slow = bool)

            out.save("nqueen.mp3")
            os.system("start nqueen.mp3")

            # Need to add mp3 remove option
            if save:
                print("Audio file saved as nqueens.mp3")

        except Exception as ex:
            print(ex)