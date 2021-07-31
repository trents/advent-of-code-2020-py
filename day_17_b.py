""" solution to Day 17b of Advent of Code 2020: https://adventofcode.com/2020/day/17 """
# Adding a 4th dimension to 17a was simple thanks to the coordinate system

def boundaries(cells):
    """ This returns an eight value array denoting the outer edges of the cells """
    edges = []
    for i in range(4):
        edges.append(min(cells, key=lambda x: x[i])[i] - 1)
        edges.append(max(cells, key=lambda x: x[i])[i] + 2)
    return edges

def get_neighbor_count(x, y, z, w, cells):
    """ Given the (x,y,z,w) coordinates and the cell network, how many active neighbors does that point have? """
    count = 0
    for tx in range(-1,2):
        for ty in range(-1,2):
            for tz in range(-1,2):
                for tw in range(-1,2):
                    if not (tx == ty == tz == tw == 0) and ((x+tx, y+ty, z+tz, w+tw) in cells):
                        count += 1
    return count

def step(cells):
    """ A single step in a 4d Conway Game of Life """
    next_cells = set()
    bounds = boundaries(cells)
    for x in range(bounds[0], bounds[1]):
        for y in range(bounds[2], bounds[3]):
            for z in range(bounds[4], bounds[5]):
                for w in range(bounds[6],bounds[7]):
                    count = get_neighbor_count(x,y,z,w,cells)
                    if (x,y,z,w) in cells and count > 1 and count < 4:
                        next_cells.add((x,y,z,w))
                    elif (x,y,z,w) not in cells and count == 3:
                        next_cells.add((x,y,z,w))
    return next_cells

cells = set()

with open("day-17.txt") as file:
    d = file.readlines()

for y,line in enumerate(d):
    for x,cell in enumerate(line):
         if cell == "#":
             cells.add((x,y,0,0))

iter = cells.copy()
print(len(step(step(step(step(step(step(iter))))))))

