from itertools import combinations, starmap
from helper    import lines_from_day
from operator  import add

nums = list(map(int, lines_from_day(9)))

def find_invalid_xmas_indices(nums):
    def not_valid_at(i): # i in [26, len(nums))
        prec, n = nums[i-25:i], nums[i]
        return n not in starmap(add, combinations(prec, 2))
    return list(filter(not_valid_at, range(26, len(nums))))

idxs = find_invalid_xmas_indices(nums) 
print("part 1:", idxs, list(map(nums.__getitem__, idxs)))

def find_weakness(nums, m):
    for n in range(2, len(nums)):
        for i in range(len(nums)-n):
            span = nums[i:i+n]
            if sum(span) == m:
                return max(span) + min(span)

print("part 2:",  find_weakness(nums, nums[idxs[0]]))

