import os, sys

def lines_from_day(n):
    fname = f"data/day{n}.txt"

    if not os.path.exists(fname):
        print(f"Data-file {fname} does not exist!\nPlace data here, then re-run.")
    else:
        with open(fname) as infile:
            for line in infile:
                yield line.strip()
