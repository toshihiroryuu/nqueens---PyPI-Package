# N-Queen problem

The aim of N-Queens Problem is to place N queens on an N x N chessboard, in a way so that no queen is in conflict with the others and finding all solutions that are possible.

Conflict is raised when two Queens are in the same row, column, or diagonal.

# Bactracking 

A backtracking algorithm tries to build a solution to a computational problem incrementally. Whenever the algorithm needs to decide between multiple alternatives to the next
component of the solution, it simply tries all possible options recursively.The idea is to place queens one by one in different columns, starting from the leftmost column, in the 
first row. When we place a queen in a column, we check for conflicts with already placed queens. In the current column, if we find a row for which there is no conflict, we mark
this row and column as part of the solution. If we do not find such a row due to conflicts then we backtrack and return false.

The expected output for this problem is a binary array which has 1s for the blocks where queens are placed, and 0s for the blocks where queens are not placed.

# Implementation

We have implemented N-Queens problem as a python package. 

So you need to install the package for finding out the solutions. 
Use Command : <code><b>pip install nqueens</b></code>

After Installing the python package import all from the nqueens package.
Use Command : <code><b>from nqueens import *</b></code>

Now we able to use all the fuctionalities of the package:

1. To know the No of solutions, Solution space and the Position of the queen
   Use Command : <code><b>qq = Queen(5, "backtrack")</b></code>
                 <code><b>qq.pprint()</b></code> 


