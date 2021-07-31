""" solution to Day 17a of Advent of Code 2020: https://adventofcode.com/2020/day/17 """
# The hardest part was figuring out how to store the cube
# I decided to use coordinates in a set
# I originally used an awful class to store it but it was more trouble than it was worth

def boundaries(cells):
    """ This returns a six value array denoting the outer edges of the cells """
    edges = []
    for i in range(3):
        edges.append(min(cells, key=lambda x: x[i])[i] - 1)
        edges.append(max(cells, key=lambda x: x[i])[i] + 2)
    return edges

def get_neighbor_count(x, y, z, cells):
    """ Given the (x,y,z) coordinates and the cell network, how many active neighbors does that point have? """
    count = 0
    for tx in range(-1,2):
        for ty in range(-1,2):
            for tz in range(-1,2):
                if not (tx == ty == tz == 0) and ((x+tx, y+ty, z+tz) in cells):
                    count += 1
    return count

def step(cells):
    """ A single step in a 3d Conway Game of Life """
    next_cells = set()
    bounds = boundaries(cells)
    for x in range(bounds[0], bounds[1]):
        for y in range(bounds[2], bounds[3]):
            for z in range(bounds[4], bounds[5]):
                count = get_neighbor_count(x,y,z,cells)
                if (x,y,z) in cells and count > 1 and count < 4:
                    next_cells.add((x,y,z))
                elif (x,y,z) not in cells and count == 3:
                    next_cells.add((x,y,z))
    return next_cells

cells = set()

with open("day-17.txt") as file:
    d = file.readlines()

for y,line in enumerate(d):
    for x,cell in enumerate(line):
         if cell == "#":
             cells.add((x,y,0))

iter = cells.copy()
print(len(step(step(step(step(step(step(iter))))))))

