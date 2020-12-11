from helper import lines_from_day, buildlist

input = buildlist(int, lines_from_day(10))
adapters  = [0] + list(sorted(input)) + [max(input)+3]

differences = buildlist(
    lambda i: adapters[i+1] -  adapters[i], range(len(adapters)-1)
)

print("part 1:", differences.count(3) * (differences.count(1)))

# shameless (and awestruck'd) copy of Todd Ginsbergs beautiful Kotlin
# solution at https://todd.ginsberg.com/post/advent-of-code/2020/day10/
def count_valid_arrangements():
    paths = {0: 1}

    for a in adapters[1:]:
        paths[a] = sum(paths.get(a-d, 0) for d in [1,2,3])

    return paths[max(adapters)]


print("part 2:", count_valid_arrangements())
