# N-Queen Problem

The N-Queens Problem is placing of N-Queens in a N * N chessboard in such a way that no queens attack each other. Queens attack each other when not more than one queen can be placed in same row or column or left daigonal or right diagonal. Backtracking algorithm is used here.

The expected output for this problem is a binary array which has 1s for the cells where queens are placed, and 0s for the blocks where queens are not placed.

# Implementation

We have implemented N-Queens problem as a python package. 

So you need to install the package for finding out the solutions. 
 <dl><code><b>pip install nqueens</b></code></dl>

After Installing the python package import all from the nqueens package.
 <dl><code><b>from nqueens import *</b></code></dl>

Now we able to use all the fuctionalities of the package:

1. To know the No of solutions, Solution space and the Position of the queen. Inputs are Number of Queens and algorithm used.
    <dl><code><b>qq = Queen(5,algo = "backtrack")</b></code></dl>
    <dl><code><b>qq.pprint()</b></code> </dl>
                 
2. To know the No of solutions, Solution space and the Positions of the queen without mentioning the input value. Input is algorithm used.
    <dl><code><b>qq = Queen(2,algo = "backtrack")</b></code></dl>
    <dl><code><b>qq.pprint()</b></code></dl>
    
3. To know the No of solutions, Solution space and the Positions of the queen by scaning a picture that have fixed rows and columns. Input is type of algorithm used and an image 
   which has table with rows and columns as in chess board.
     <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q5.PNG")</b></code></dl>
     <dl><code><b>qq.pprint()</b></code></dl>

4. To Get voice output of the No of solutions, Solution space and the Positions of the queen by scaning a picture that have fixed rows and columns. Input is type of algorithm 
   used and an image which has table with rows and columns as in chess board.
     <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q4.png")</b></code></dl>
     <dl><code><b>qq.pprint()</b></code></dl>
     <dl><code><b>qq.alexa()</b></code></dl>
     
5. To Display output as a nxn Table form, No of solutions, Solution space and the Positions of the queen. Input is type of algorithm used and an image which has table with rows
   and columns as in chess board.
     <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q4.png")</b></code></dl>
     <dl><code><b>qq.pprint()</b></code></dl>
     <dl><code><b>qq.display()</b></code></dl>
     
6. To Display output as a nxn Table form, No of solutions, Solution space and the Positions of the queen. Input is type of algorithm used and an image which has table with rows
   and columns as in chess board.
     <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q4.png")</b></code></dl>
     <dl><code><b>qq.pprint()</b></code></dl>
     <dl><code><b>qq.display()</b></code></dl>
     
7. To Get output and locally save the nxn Table form as an image, No of solutions, Solution space and the Positions of the queen. Input is type of algorithm used and an image
   which has table with rows and columns as in chess board.
     <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q4.png")</b></code></dl>
     <dl><code><b>qq.pprint()</b></code></dl>
     <dl><code><b>qq.display()</b></code></dl>
     
     
Special Credits: https://github.com/garthur 
References: https://www.geeksforgeeks.org/n-queen-problem-backtracking
