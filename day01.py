import utils

stringrep = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

processed_input = utils.process_raw_input("day1.input")

def solve(lines, part2=False):
    summation = 0
    for line in lines:
        digits = []
        s = ""
        for c in line:
            if c.isnumeric():
                digits.append(c)
            else:
                s = s+c
            if part2:
                for key in stringrep.keys():
                    if key in s:
                        digits.append(stringrep[key])
                        s = s[-1]
        try:
            summation += (int(digits[0])*10 + int(digits[-1]))
        except:
            pass
    return summation
print(solve(processed_input))
print(solve(processed_input, True))