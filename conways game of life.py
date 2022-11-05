size_of_grid = 10
number_of_cycles = 10
grid = [['O' for x in range(size_of_grid)] for y in range(size_of_grid)]
temp_grid = [['O' for x in range(size_of_grid)] for y in range(size_of_grid)]
grid[1][2] = 'X'
grid[2][2] = 'X'
grid[3][2] = 'X'
grid[3][1] = 'X'
grid[2][0] = 'X'

for i in range(size_of_grid):
    print(grid[i])
print('-')

for a in range(number_of_cycles):
    for x in range(size_of_grid):
        for y in range(size_of_grid):
            temp_grid[y][x] = grid[y][x]
    for x in range(size_of_grid):
        for y in range(size_of_grid):
            neighbours = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if ((y+j)>=0)and((y+j)<size_of_grid)and((x+i)>=0)and((x+i)<size_of_grid):
                        if grid[y+j][x+i] == 'X':
                            neighbours+=1
            if grid[y][x] == 'X':
                neighbours-=1
            if (neighbours < 2) or (neighbours > 3):
                temp_grid[y][x]='O'
            if neighbours == 3:
                temp_grid[y][x]='X'
    for x in range(size_of_grid):
        for y in range(size_of_grid):
            grid[y][x] = temp_grid[y][x]
    for i in range(size_of_grid):
        print(grid[i])
    print("-")
