P1ROCK = "A"
P1PAPER = "B"
P1SCISSORS = "C"
P2ROCK = P2LOSE = "X"
P2PAPER = P2DRAW = "Y"
P2SCISSORS = P2WIN = "Z"


def calc_win(p1, p2):
    if p1 == P1ROCK:
        if p2 == P2PAPER:
            return 6
        elif p2 == P2SCISSORS:
            return 0
    elif p1 == P1PAPER:
        if p2 == P2ROCK:
            return 0
        elif p2 == P2SCISSORS:
            return 6
    else:  # p1 == P1SCISSORS
        if p2 == P2ROCK:
            return 6
        elif p2 == P2PAPER:
            return 0
    return 3


def check_played(p):
    if p == P2ROCK:
        return 1
    elif p == P2PAPER:
        return 2
    return 3


def p1top2(p):
    if p == P1ROCK:
        return P2ROCK
    elif p == P1PAPER:
        return P2PAPER
    return P2SCISSORS


def calc_played(p1, p2):
    if p2 == P2WIN:
        if p1 == P1ROCK:
            return check_played(P2PAPER)
        elif p1 == P1PAPER:
            return check_played(P2SCISSORS)
        return check_played(P2ROCK)
    elif p2 == P2LOSE:
        if p1 == P1ROCK:
            return check_played(P2SCISSORS)
        elif p1 == P1PAPER:
            return check_played(P2ROCK)
        return check_played(P2PAPER)
    else:
        return check_played(p1top2(p1))


def check_win(p2):
    if p2 == P2LOSE:
        return 0
    elif p2 == P2DRAW:
        return 3
    return 6


if __name__ == "__main__":
    with open("input2") as f:
        games = []
        for game in f:
            games.append(game.split())

    total = 0
    for p1, p2 in games:
        total += calc_win(p1, p2)
        total += check_played(p2)

    print(total)

    total = 0
    for p1, p2 in games:
        total += calc_played(p1, p2)
        total += check_win(p2)

    print(total)
