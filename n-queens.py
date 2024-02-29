import numpy as np

n = int(input())
board = []

def empty_board():
      global board
      board = np.full((n, n), 0)
counter = 0

def update(i, j):
      board[i] = 1
      board[:,j]=1

      diagnol = board[i:, j:n+1]
      np.fill_diagonal(diagnol, 1)
      board[i:, j:n+1]=diagnol

      diagnol = board[i:, 0:j+1]
      np.fill_diagonal(np.fliplr(diagnol), 1)
      board[i:, 0:j+1]=diagnol

      diagnol = board[0:i+1, j:n+1]
      np.fill_diagonal(np.flipud(diagnol), 1)
      board[0:i+1, j:n+1]=diagnol

      diagnol = board[0:i+1, 0:j+1]
      np.fill_diagonal(np.flip(diagnol), 1)
      board[0:i+1, 0:j+1]=diagnol

def update_squares(a):
      global stack
      global res
      global test_stack
      res = np.argwhere(board == 0)
      res = res.tolist()
      test_stack=[]
      for l in res:
            if l[0]==a:
                  test_stack.append(l)
      for l in test_stack:
            stack.append(l)

for j in range(n):
      empty_board()
      update(0, j)
      print(board)
      stack=[]
      update_squares(1)
      print(stack)
      visited = []
      visited_board = []
      visited_board.append(board)
      print(visited_board)
      while len(stack)>0:
            check_visited = False
            v = stack.pop()
            for u in visited:
                  if u==v:
                        check_visited=True
            if check_visited == False:
                  visited.append(v)
                  if len(visited_board)!=v[0]:
                        visited_board = visited_board[0:v[0]]
                        visited = visited[0:v[0]]
                  board = np.array(visited_board[-1])
                  update(v[0], v[1])
                  update_squares(v[0]+1)
                  visited_board.append(board)
                  if v[0]==n-1:
                        counter=counter+1
                  print(v)
                  print(board)
                  print('visited', visited)
                  print('stack', stack)
                  print(visited_board)
                  
print(counter)