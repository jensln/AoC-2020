from helper import lines_from_day
from itertools import product
import numpy as np

tiles = np.array(list(list(line) for line in lines_from_day(11)))

w, l = tiles.shape

def count(ts, tt, i,j):
    marray = np.ma.array(ts)
    marray[i, j] = np.ma.masked
    region = marray[
        np.clip((i-1), 0, w) : np.clip((i+2), 0, w), # 3x3 area
        np.clip((j-1), 0, l) : np.clip((j+2), 0, l)  # c. (i,j)
    ]
    return np.sum(region == tt)

def next_from(ts, i,j):
    t = ts[i,j]
    return {
        "L": "#" if (count(ts, "#", i, j) == 0) else t,
        "#": "L" if (count(ts, "#", i, j) >= 4) else t
    }.get(t, t)

# this method is _extremely_ inefficient.
#
# completes after 7 minutes on my laptop.
# I guess expressibility comes at a cost
# of effectivity; and my numpy-usage is
#  for certain less than sub-optimal ...

prev = tiles
next = np.empty_like(tiles, dtype=np.object)

while True:
    for (i,j) in product(range(w), range(l)):
        next[i,j] = next_from(prev, i, j)
    if np.all(prev == next): break
    prev = next.copy()

print("part 1:", np.sum(next == "#"))

# I haven't bothered with part 2
