import copy
from sys import stdin
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



grid=[]
for line in stdin:
    line=line.replace('\n','')
    if line == "":
        break
    grid.append(list(line))

width=len(grid[0])
height=len(grid)

print(f"Grid is {width}x{height}")

total_rolls=0
print_grid=copy.deepcopy(grid)
for y in range(height):
    for x in range(width):
        if is_paper_roll(grid[y][x]) and has_fewer_than_four_neighbors(grid,x,y):
            print_grid[y][x] = 'x'
            total_rolls+=1

for line in print_grid:
    for char in line:
        print(char,end='')
    print()

print(f"There are {total_rolls} rolls of paper that can be accessed by a forklift.")
