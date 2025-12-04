import copy
import time
from sys import stdin
import sys
from io import StringIO


FPS=10

def is_paper_roll(char):
    return char == '@'

def is_inside_grid(grid,x,y):
    width=len(grid[0])
    height=len(grid)
    return x>=0 and x<width and y>=0 and y<height

def has_fewer_than_four_neighbors(grid, x, y):
    neighbors=0

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i==0 and j==0:
                continue
            if is_inside_grid(grid,x+j,y+i) and is_paper_roll(grid[y+i][x+j]):
                neighbors+=1

    return neighbors<4

def pretty_print_grid(grid):
    conversion_table = {'.': "\033[40m  \033[m", 'x': "\033[44m  \033[m", '@': "\033[41m  \033[m"}
    buf = StringIO() # solve flickering when printing

    buf.write('\n')
    buf.write('\n')
    buf.write('\n')

    for line in grid:
        for char in line:
            buf.write(conversion_table[char])
        buf.write('\n')
    sys.stdout.write(buf.getvalue())
    sys.stdout.flush()



grid=[]
for line in stdin:
    line=line.replace('\n','')
    if line == "":
        break
    grid.append(list(line))


width=len(grid[0])
height=len(grid)

#print(f"Grid is {width}x{height}")
pretty_print_grid(grid)
time.sleep(2.5)

total_rolls=0
new_grid=copy.deepcopy(grid)

while True:
    new_rolls=0
    for y in range(height):
        for x in range(width):
            if is_paper_roll(grid[y][x]) and has_fewer_than_four_neighbors(grid,x,y):
                new_grid[y][x] = 'x'
                new_rolls+=1
    total_rolls+=new_rolls
    grid=copy.deepcopy(new_grid)

    #print(f"Remove {new_rolls} rolls of paper:")
    #for line in new_grid:
    #    for char in line:
    #        print(char,end='')
    #    print()
    pretty_print_grid(new_grid)
    time.sleep(1/FPS)

    if new_rolls==0:
        break


#print(f"There are {total_rolls} rolls of paper that can be accessed by a forklift.")
