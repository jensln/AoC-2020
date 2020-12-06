from helper import sections_from_day, buildlist

# a list of list og sets... being a list of "groups"
# (also a list) containing sets of answers per individual
groups = buildlist(lambda gs: buildlist(set, gs),
                   sections_from_day(6))

n1 = sum(map(lambda gs: len(set().union(*gs)), groups))

print("part 1:", n1)

n2 = sum(map(lambda gs: len(gs[0].intersection(*gs)), groups))

print("part 2:", n2)

