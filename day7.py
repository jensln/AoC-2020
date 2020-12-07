from helper import lines_from_day
import re
from functools import cache

re_inner_bag = re.compile(r"(\d+) ([\w\s]+) bags?")

def split(line):
    return line.split(" bags contain ")

bdict = { (ps := split(line))[0] :
            { bag : int(n) for n,bag
                         in re_inner_bag.findall(ps[1]) }
          for line in lines_from_day(7) }

@cache
def search(s, bk):
    "True if bk contains s or if any of search(s, d) where d in bk"
    b = set(bdict[bk].keys())
    return (s in b) or bool(b) and any(search(s, bn) for bn in b)

n1 = sum(search("shiny gold", bag) for bag in bdict.keys())

print("part 1:", n1)

def count_inner_bags(bk, *, _d=0):
    b = set(bdict[bk].keys())
    return sum(
        bdict[bk][bn]*count_inner_bags(bn, _d=_d+1) for bn in b
    ) + int(bool(_d)) # add one for every bag but the first

n2 = count_inner_bags("shiny gold")

print("part 2:", n2)
