from helper import lines_from_day
import numpy as np

def traverse(dx, dy):
    lines = list(lines_from_day(3) 
    h, w = len(lines), len(lines[0])
    return list(lines[i*dy][i*dx % w] for i in range(h // dy))

path = traverse(3, 1)

print((np.array(path) == '#').sum())

vels = [(1,1), (3,1), (5,1), (7,1), (1, 2)]

trees_for_vels = [ (np.array(traverse(dx, dy)) == '#').sum()
                        for (dx, dy) in vels ]

print(np.array(trees_for_vels).prod())

