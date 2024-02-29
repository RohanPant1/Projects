visited_board = []
def transversal():
    global stack
    if position[0]+2<n and position[1]+1<n:
        stack.append([position[0]+2, position[1]+1])
    if position[0]-2>0 and position[1]+1<n:
        stack.append([position[0]-2, position[1]+1])
    if position[0]+1<n and position[1]+2<n:
        stack.append([position[0]+1, position[1]+2])
    if position[0]-1>0 and position[1]+2<n:
        stack.append([position[0]-1, position[1]+2])
def change_position(a, b):
    global position
    global board
    global pawns
    global max
    board[position[0]][position[1]] = '.'
    position = [a, b]
    board[position[0]][position[1]] = 'K'
    max_cell = pawns
    for i in range(n):
        for j in range(n):
            if board[i][j]=='P':
                max_cell = max_cell -1
    if max_cell>max:
        max = max_cell

t =int(input())
for i in range(t):
    n = int(input())
    board = []
    pawns = 0
    max = 0
    for j in range(n):
        l =  input()
        test = []
        for letter in l:
            test.append(letter)
            if letter == 'P':
                pawns = pawns +1
        board.append(test)
    for lists in range(n):
        for letter in range(n):
            if board[lists][letter]=='K':
                position = [lists, letter]
    print(pawns)
    stack = []
    transversal()
    visited = []
    visited_position = []
    visited_board.append(board)
    visited_position.append(position)
    print(visited)
    print(stack)
    print(position)
    print(board)
    print(visited_board)
    print('gap')
    while len(stack)>0:
        check_visited = False
        v = stack.pop()
        for u in visited:
            if u==v:
                check_visited = True
        if check_visited == False:
            visited.append(v)
            # while visited_position[-1][1]>position[1]:
            #     del visited_position[-1]
            #     del visited_board[-1]
            # board = visited_board[-1]
            change_position(v[0], v[1])
            transversal()
            visited_board.append(board)
            visited_position.append(position)
            print(position)
            print(visited)
            print(visited_position)
            print(board)
            print(visited_board)
            print(stack)
            print('gap')
    print(max)