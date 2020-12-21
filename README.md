# N-Queen Problem

The N-Queens Problem is placing of N-Queens in a N * N chessboard in such a way that no queens attack each other. Queens attack each other when not more than one queen can be placed in same row or column or left daigonal or right diagonal. Backtracking algorithm is used here.

The expected output for this problem is a in the form of 1s and 0s, 1s for the cells where queens are placed, and 0s for the blocks where queens are not placed.

# Implementation

Install the package for finding N-Queen Solutions. 
 <dl><code><b>pip install nqueens</b></code></dl>

Import classes from the package.
 <dl><code><b>from nqueens import *</b></code></dl>
  
1. <b>N Queens Solutions </b>
    <dl><code><b>qq = Queen(5,algo = "backtrack")</b></code></dl>
    <dl><code><b>qq.pprint()</b></code> </dl>
                 
2. <b>N Queens Solutions when input is type of algorithm used</b>
    <dl><code><b>qq = Queen(algo = "backtrack")</b></code></dl>
    <dl><code><b>qq.pprint()</b></code></dl>
    
3. <b>N Queens Solution when input is an image (Blank table with rows and columns as in chess board).</b>
     ![image](https://github.com/toshihiroryuu/nqueens---PyPI-Package/blob/main/tests/q4b.PNG)
     <dl><code><b>qq = Queen(4, algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q5.PNG")</b></code></dl>

4. <b>N Queens Solution as Voice output </b> 
     <dl><code><b>qq = Queen(4, algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.alexa()</b></code></dl>
     
5. <b>N Queens Solution as Table output </b>
     <dl><code><b>qq = Queen(4, algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.display()</b></code></dl>
     
6. <b>N Queens Solution as PNG File output </b>
     <dl><code><b>qq = Queen(4, algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.save()</b></code></dl>
     
     
     
<dl>Special Credits: https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html </dl>
<dl>References: https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/ </dl>
