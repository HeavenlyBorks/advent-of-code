import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        elves = []
        current = []
        for cal in f:
            if cal == "\n":
                elves.append(sum(current))
                current = []
            else:
                current.append(int(cal.strip()))
        # don't forget the last elf :(
        elves.append(sum(current))

    for _ in range(3):
        print(max(elves))
        elves.remove(max(elves))
