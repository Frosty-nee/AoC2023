import utils
import string
import math

class number:
    value = 0
    coordinates = set()
    def __init__(self, start, end, line):
        self.coordinates = set()
        value = 0
        for x in range(start, end+1):
            if type(processed_input[line][x]) == int:
                value = (value*10)+processed_input[line][x]
            self.coordinates.add((x, line))
        self.value = value

    def __str__(self):
        return "Value: {}, Coords: {}".format(self.value, self.coordinates)


class symbol:
    row, column = None, None
    adjacent_coordinates = None
    def __init__(self, coordinates):
        self.row, self.column = coordinates
        self.value = processed_input[self.row][self.column]
        self.adjacent_coordinates = set()
        for y in range(self.row-1, self.row +2):
            for x in range(self.column-1, self.column +2):
                self.adjacent_coordinates.add((x,y))

    def __str__(self):
        return "Coordinates: {} Adjacents {}".format((self.column, self.row), self.adjacent_coordinates)

def find_symbols():
    symbols = set()
    for y in range(len(processed_input)):
        for x in range(len(processed_input[y])):
            if (value:= processed_input[y][x]) and type(value) == str:
                symbols.add(symbol((y,x)))
    return symbols

def find_numbers():
    numbers = []
    for line in range(len(processed_input)):
        starts = find_number_starts(processed_input[line])
        ends = find_number_ends(processed_input[line])
        for index in range(len(starts)):
            numbers.append(number(starts[index], ends[index], line))
    return numbers

def find_number_starts(line):
    starts = []
    for char in range(len(line)):
        if line[char] != None and type(line[char]) == int and (line[char-1] == None or type(line[char-1]) != int):
            starts.append(char)
    return starts

def find_number_ends(line):
    ends = []
    for char in range(len(line)-1, -1, -1):
        if char >= len(line)-1 or (line[char] != None and type(line[char]) == int and (line[char+1] == None or type(line[char+1]) == str)):
            ends.append(char)
    ends.reverse()
    return ends

def is_number_adjacent_to_symbol(number):
    for symbol in symbols:
        for coordinate in symbol.adjacent_coordinates:
            if coordinate in number.coordinates:
                return True
    return False


if __name__ == "__main__":
    raw_input = utils.process_raw_input("day3.input")

    processed_input = [[int(char) if char in string.digits else char if (char in string.punctuation and char != '.') else None for char in line] for line in raw_input]
    total = 0
    symbols = find_symbols()
    numbers = find_numbers()
    for number in numbers:
        if is_number_adjacent_to_symbol(number) :
            total+=number.value

    gear_ratio_total = 0
    for symbol in symbols:
        if symbol.value == '*':
            adjacent_numbers = set()
            for number in numbers:
                if len(number.coordinates.intersection(symbol.adjacent_coordinates)) > 0:
                    adjacent_numbers.add(number)
            if len(adjacent_numbers) == 2:
                gear_ratio_total += adjacent_numbers.pop().value * adjacent_numbers.pop().value

    print(total)
    print(gear_ratio_total)