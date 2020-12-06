from helper import sections_from_day
import re

entries = sections_from_day(4, concat=True, split=" ")

required_fields = set(
    ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
)

n1 = sum([( set(map(lambda s: s.split(":")[0], entry))
              >= required_fields)
                   for entry in entries ])

print("part 1:", n1)

def validate(entry):
    d = dict(map(lambda s: s.split(":"), entry))

    if not set(d.keys()) >= required_fields:
        return False

    def constrain_year(ys, min, max):
        return len(ys) == 4 and min <= int(ys) <= max  # ys is a string

    def check_height(hs):
        unit = "cm" if hs.endswith("cm") else ("in" if hs.endswith("in") else None)
        if unit:
            h = int(hs[:-2])
            return (150 <= h <= 193) if (unit == "cm") else (59 <= h <= 76)
        else:
            return False

    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    return all(
        [ constrain_year(d['byr'], 1920, 2002),
          constrain_year(d['iyr'], 2010, 2020),
          constrain_year(d['eyr'], 2020, 2030),
          check_height(d['hgt']),
          re.search("^#[0-9a-f]{6}$", d['hcl']),
          any(map(lambda s: d['ecl'] == s, valid_eye_colors)),
          re.search("^[0-9]{9}$", d['pid'])
        ]
    )

n2 = sum(map(validate, entries))

print("part 2:", n2)
