import tkinter as tk
import sudoku as Sudoku
import requests

sudoku_puzzle = [[6, 2, 5, 8, 4, 3, 7, 9, 1],
[7, 9, 1, 2, 6, 5, 4, 8, 3],
[4, 8, 3, 9, 7, 1, 6, 2, 5],
[8, 1, 4, 5, 9, 7, 2, 3, 6],
[2, 3, 6, 1, 8, 4, 9, 5, 7],
[9, 5, 7, 3, 2, 6, 8, 1, 4],
[5, 6, 9, 4, 3, 2, 1, 7, 8],
[3, 4, 2, 7, 1, 8, 5, 6, 9],
[1, 7, 8, 6, 5, 9, 3, 4, 2]]

initial_puzzle=[[6, -1, -1, -1, -1, 3, -1, -1, 1],
[-1, 9, -1, -1, -1, -1, -1, -1, 3],
[4, -1, 3, -1, -1, -1, 6, -1, -1],
[-1, -1, -1, 5, 9, -1, 2, -1, 6],
[-1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, 7, -1, -1, -1, -1, -1, 4],
[-1, -1, -1, -1, -1, -1, 1, 7, -1],
[-1, -1, 2, -1, -1, 8, -1, -1, -1],
[-1, -1, 8, -1, -1, -1, -1, 4, 2]]
final_puzzle = []
row_puzzle = []
window = tk.Tk()
widgets = {}
a = 1
for r in range(9):
   for c in range(9):
      if initial_puzzle[r][c]==-1:
         b= tk.Entry(window, font=('Arial 24'), width=2)
         b.grid(row=r,column=c) 
         widgets[(r,c)] = b
      else:
         b = tk.Label(window, height=2, width=4, text=initial_puzzle[r][c],)
         b.grid(row=r,column=c)
         widgets[(r, c)] = b

def check_grid():
   global row_puzzle
   global final_puzzle
   print(window.grid_slaves(0, 1)[0])
   print(widgets[(0, 1)].get())
   for r in range(9):
      for c in range(9):
         if isinstance(widgets[(r, c)], tk.Entry):
            row_puzzle.append(widgets[(r, c)].get())
         else:
            row_puzzle.append(widgets[(r, c)]['text'])
      final_puzzle.append(row_puzzle)
      row_puzzle = []
   if final_puzzle == sudoku_puzzle:
      tk.Label(window, text="You won!").grid(row=12, column=11, pady=20)
   else:
      tk.Label(window, text="try again").grid(row=12, column=11, pady=20)
   print(final_puzzle)
   print(sudoku_puzzle)

submit = tk.Button(window, text="Submit",height=2, width=10, command=check_grid).grid(row=11, column=11, pady=20, padx=10)

window.mainloop()