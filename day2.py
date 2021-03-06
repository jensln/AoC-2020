from collections import Counter
from helper import lines_from_day

def parse():
    for line in lines_from_day(2):
        words = line.split(" ")
        rdesc = words[0].split("-")
        a, b = int(rdesc[0]), int(rdesc[1])
        char = words[1][0];  string = words[2]
        yield (a, b, char, string)

input = list(parse())

n1 = sum([ min <= Counter(w)[c] <= max
             for (min, max, c, w) in input ])

print(n1)

n2 = sum([ (w[a-1]==c) ^ (w[b-1]==c)
             for (a, b, c, w) in input ])

print(n2)
