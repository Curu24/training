import random

empty = '.'
snk = '#'
dot = '@'
field = []
side = 10

for i in range(side):
    field.append([])
    for j in range(side):
        field[i].append(empty)

x, y = (side//2), (side//2)
field[x][y] = snk
snake = []
snake.append((x, y))
dotx = random.randrange(side)
doty = random.randrange(side)
field[dotx][doty] = dot

for i in range(side):
    for j in range(side):
        print(field[i][j], end='')
    print('')

while True:
    listener = input()

    # Move up
    if listener == 'w':
        if (x-1) < 0 or field[x-1][y] == snk:
            print("Game over\nScore: ", len(snake))
            break
        elif field[x-1][y] == dot:
            x = x - 1
            snake.append((x, y))
            field[x][y] = snk
            dotx = random.randrange(side)
            doty = random.randrange(side)
            field[dotx][doty] = dot
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')
        else:
            field[snake[0][0]][snake[0][1]] = empty
            x = x - 1
            snake.append((x, y))
            snake.pop(0)
            field[x][y] = snk
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')

    #Move down
    if listener == 's':
        if (x+1) > (side-1) or field[x+1][y] == snk:
            print("Game over\nScore: ", len(snake))
            break
        elif field[x+1][y] == dot:
            x = x + 1
            snake.append((x, y))
            field[x][y] = snk
            dotx = random.randrange(side)
            doty = random.randrange(side)
            field[dotx][doty] = dot
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')
        else:
            field[snake[0][0]][snake[0][1]] = empty
            x = x + 1
            snake.append((x, y))
            snake.pop(0)
            field[x][y] = snk
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')

    #Move left
    if listener == 'a':
        if (y-1) < 0 or field[x][y-1] == snk:
            print("Game over\nScore: ", len(snake))
            break
        elif field[x][y-1] == dot:
            y = y - 1
            snake.append((x, y))
            field[x][y] = snk
            dotx = random.randrange(side)
            doty = random.randrange(side)
            field[dotx][doty] = dot
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')
        else:
            field[snake[0][0]][snake[0][1]] = empty
            y = y - 1
            snake.append((x, y))
            snake.pop(0)
            field[x][y] = snk
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')

    #Move right
    if listener == 'd':
        if (y+1) > (side-1) or field[x][y+1] == snk:
            print("Game over\nScore: ", len(snake))
            break
        elif field[x][y+1] == dot:
            y = y + 1
            snake.append((x, y))
            field[x][y] = snk
            dotx = random.randrange(side)
            doty = random.randrange(side)
            field[dotx][doty] = dot
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')
        else:
            field[snake[0][0]][snake[0][1]] = empty
            y = y + 1
            snake.append((x, y))
            snake.pop(0)
            field[x][y] = snk
            for i in range(side):
                for j in range(side):
                    print(field[i][j], end='')
                print('')
