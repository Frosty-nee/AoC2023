import utils
from datetime import datetime

games = utils.process_raw_input("day2.input")
def solve(games, part2=False):
    summation = 0
    for game in games:
        id = int(game.split(":")[0].split(" ")[1])
        cubes = {}
        for look in game.split(":")[1].split(";"):
            for cubetype in look.split(","):
                count, color = cubetype.strip().split(" ")
                if color not in cubes.keys():
                    cubes[color] = int(count)
                elif cubes[color] < int(count):
                        cubes[color] = int(count)

        if part2:
             summation += (cubes["red"] * cubes["green"] * cubes["blue"])
        elif cubes["red"] > 12 or cubes["green"] > 13 or cubes["blue"] > 14:
            pass
        else:
             summation += id
    return summation
start = datetime.utcnow()
print(solve(games))
start2 = datetime.utcnow()
print(solve(games, True))