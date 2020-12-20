# N-Queen Problem

The N-Queens Problem is placing of N-Queens in a N * N chessboard in such a way that no queens attack each other. Queens attack each other when not more than one queen can be placed in same row or column or left daigonal or right diagonal. Backtracking algorithm is used here.

The expected output for this problem is a in the form of 1s and 0s, 1s for the cells where queens are placed, and 0s for the blocks where queens are not placed.

# Implementation

Install the package for finding N-Queen Solutions. 
 <dl><code><b>pip install nqueens</b></code></dl>

Import classes from the package.
 <dl><code><b>from nqueens import *</b></code></dl>

1. <b>Inputs : Number of Queens , type of algorithm used</b>
    <dl><code><b>qq = Queen(5,algo = "backtrack")</b></code></dl>
    <dl><code><b>qq.pprint()</b></code> </dl>
                 
2. To know the No of solutions, Solution space and the Positions of the queen without mentioning the input value. Input is algorithm used.
    <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
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
     
     
<dl>Special Credits: https://github.com/garthur </dl>
<dl>References: https://www.geeksforgeeks.org/n-queen-problem-backtracking </dl>
