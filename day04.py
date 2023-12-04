import utils
import math
import string

def scratchcard_value(scratchcard):
    return(int(math.pow(2, len(scratchcard.winners.intersection(scratchcard.numbers))-1)))

def parse_scratchcards():
    scratchcards = []
    for card in raw_input:
        cardno, numbers = card.split(": ")
        cardno = cardno.split(" ")[1]
        winners = set()
        contestants = set()
        winning_numbers, contest_numbers = numbers.split(" | ")
        for winner in winning_numbers.split(" "):
            if winner != '' :
                winners.add(int(winner))
        for contestant in contest_numbers.split(" "):
            if contestant != '':
                contestants.add(int(contestant))
        scratchcards.append(scratchcard(cardno, winners, contestants))
    return scratchcards

def solvep1():
    total = 0
    for card in cards:
        total += scratchcard_value(card)
    return total

def solvep2():
    for cardid in range(len(cards)):
        for match in range(1, len(cards[cardid].winners.intersection(cards[cardid].numbers))+1):
            cards[cardid+match].count += 1*cards[cardid].count
    total = 0
    for card in cards:
        total += card.count
    return total

class scratchcard:
    def __init__(self, id, winners, numbers, count=1):
        self.id = id
        self.count = count
        self.winners = winners
        self.numbers = numbers
    def __str__(self):
        return "ID: {}\nCount: {}\nWinning Numbers: {}\nTest Numbers: {}\nIntersection: {}".format(self.id, self.count, self.winners, self.numbers, self.winners.intersection(self.numbers))

if __name__=="__main__":
    raw_input = utils.process_raw_input("day4.input")
    cards = parse_scratchcards()
    print(solvep1())
    print(solvep2())