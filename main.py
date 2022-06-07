from collections import deque

n = int(input())

board = [([0] * n) for _ in range(n)]

apple = []
k = int(input())
for _ in range(k):
    input_row, input_col = map(int, input().split())

    apple_row, apple_col = input_row - 1, input_col -1

    board[apple_row, apple_col] = 1

    apple.append((apple.row, apple.col))



L = int(input())
change_snake = []
for _ in range(L):

    dis, direct = input().split()
    dis = int(dis)
    change_snake.append((dis, direct))

change_snake.append((10001, ''))

change = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_snake(direction):
    global turn_index

    if direction == 'L':
        if turn_index != 0:
            turn_index -=1
        else:
            turn_undex = 3
    else:
        if turn_index != 3:
            turn_index += 1
        else:
            turn_index = 0
    return

snake = deque()
snake.append((0, 0))

turn_index = 1

x, y, = 0, 0

cnt = 0
start = 1


breaker = False

for i in range(len(change_snake)):

    start = cnt + 1
    for _ in range(start, change_snake[i][0] +1):

        nx = x +change[turn_index][0]
        ny = y +change[turn_index][1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            cnt += 1
            breaker = True
            break
        if board[nx][ny] == 1:
            board[nx][ny]  = 0
            x, y = nx, ny

            snake.append((x,y))
        else:
            x, y = nx, ny

            snake.popleft()
            snake.append((x, y))

        cnt+=1

    if breaker == True:
        break
    turn_snake(change_snake[i][1])

print(cnt)