import os, sys

def buildlist(f, *its):
    return list(map(f, *its))

def _ensure_existance(fname):
    if not os.path.exists(fname):
        print(f"Data-file {fname} does not exist!\nPlace data here, then re-run.")
        sys.exit(1)
    return True

def lines_from_day(n):
    fname = f"data/day{n}.txt"
    if _ensure_existance(fname):
        with open(fname) as infile:
            for line in infile:
                yield line.strip()

def sections_from_day(n):
    sections = []; acc = []
    for line in lines_from_day(n):
        if bool(line.strip()): # line not blank
            acc.append(line.strip())
        else:
            sections.append(acc)
            acc = []
    if acc: # the last line might not be blank
        sections.append(acc)
    return sections

