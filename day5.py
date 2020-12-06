from helper import lines_from_day
from itertools import product

# FBFBBFFRLR -> (0101100, 101) -> (44, 5)
def read_seat(code):
    translation = str.maketrans("FBLR", "0101")
    tr = lambda s: int(s.translate(translation), base=2)
    row, col = tr(code[:7]), tr(code[7:])
    return row, col

def seat_id(p):
    r, c = p
    return 8*r+c

observed_seats = set(map(read_seat, lines_from_day(5)))

print("part 1:", max(map(seat_id, observed_seats)))

minrow, maxrow = min(observed_seats)[0], max(observed_seats)[0]
all_possible_seats = set(product(range(minrow, maxrow), range(8)))

# there is only one empty possible seat
my_seat = list(all_possible_seats - observed_seats)[0]
print("part 2:", seat_id(my_seat))
