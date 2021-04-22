# Sudoku-Solver
Python code to solve a 9x9 Sudoku Puzzle

The code takes a 9x9 matrice as input as a Sudoku Puzzle with 0 in place of empty spaces.
If the Puzzle can be solved by the 'Unique Candidate' method, it will return a tuple with True and the solution, otherwise it will retourn False and None.
The 'Unique Candidate' method verifies if there is only one possible answer for a house and fills the house with this number.
