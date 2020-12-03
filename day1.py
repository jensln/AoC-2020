from itertools import combinations
from helper import lines_from_day

numbers = list(map(int, lines_from_day(1)))

for (a,b) in combinations(numbers, 2):
    if (a+b) == 2020:
        print(f"{a} + {b} = {a+b}")
        print(f"{a} * {b} = {a*b}")

for (a,b,c) in combinations(numbers, 3):
    if (a+b+c) == 2020:
        print(f"{a} + {b} + {c} = {a+b+c}")
        print(f"{a} * {b} * {c} = {a*b*c}")
