def to_priority(l):
    if ord(l) >= 97:
        return ord(l) - 96
    elif ord(l) >= 65:
        return ord(l) - 38


if __name__ == "__main__":
    with open("input3") as f:
        rucksacks = []
        for rucksack in f:
            rucksack = rucksack.strip()
            rucksacks.append(
                [rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]]
            )

    dups = []
    for rucksack in rucksacks:
        temp = []
        for letter in rucksack[0]:
            if letter in rucksack[1]:
                temp.append(letter)
        dups.extend(set(temp))

    print("duplicates in each rucksack:", sum(to_priority(l) for l in dups))

    dups = []
    i = 0
    for i in range(0, len(rucksacks), 3):
        temp = []
        for letter in "".join(rucksacks[i]):
            if letter in "".join(rucksacks[i + 1]) and letter in "".join(
                rucksacks[i + 2]
            ):
                temp.append(letter)
        dups.extend(set(temp))

    print("duplicates in each elf group:", sum(to_priority(l) for l in dups))
