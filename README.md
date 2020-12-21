# N-Queen Problem

The "N-Queens Problem" is a classical problem of chess. Here N Queens are to be placed on an N * N chessboard in such a way that no queens attack each other. A Queen can  attack other Queens if its placed on the  same row, column or on its diagonals. We use Backtracking in the backend to solve this problem .
# Usage

To Install this package. Use :
 <dl><code><b>pip install nqueens</b></code></dl>

# Class Definition

```class Queen:

     def __init__(self, n = 0, algo = "backtrack", pos = []):
          self.n = int(n)
          self.algo = algo
          self.pos = []

          self.count = 0
          self.queen_data = []```

Use the below snippit to start using the package.
<dl><code><b>from nqueens import *</b></code></dl>

1. <b>NQueens Possible Solution Space </b>
    <dl><code><b>qq = Queen(5)</b></code></dl>
    <dl><code><b>qq.pprint()</b></code> </dl>

2. <b>Use scan_queen() class function to solve NQueens problem with image input.</b>
     ![image](https://github.com/toshihiroryuu/nqueens---PyPI-Package/blob/main/tests/q4b.PNG)
     <dl><code><b>qq = Queen(4, algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.scan_queen("q5.PNG")</b></code></dl>

3. <b>NQueens Solution space as Voice output </b>
     <dl><code><b>qq = Queen(4)</b></code></dl>
     <dl><code><b>qq.alexa()</b></code></dl>

4. <b>NQueens Solution space as image output </b>
     <dl><code><b>qq = Queen(4, algo = "backtrack")</b></code></dl>
     <dl><code><b>qq.display()</b></code></dl>

5. <b>NQueens Solution space as PNG File output </b>
     <dl><code><b>qq = Queen(4)</b></code></dl>
     <dl><code><b>qq.save()</b></code></dl>



<dl>Special Credits: https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html </dl>
<dl>References: https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/ </dl>

<dl>Visit our GitHub Repository for more information: https://github.com/toshihiroryuu/nqueens---PyPI-Package</dl>
