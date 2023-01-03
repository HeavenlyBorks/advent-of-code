import sys


def format_ranges(r1, r2):
    t1 = r1.split("-")
    t2 = r2.split("-")
    t1[0] = int(t1[0])
    t2[0] = int(t2[0])
    t1[1] = int(t1[1]) + 1
    t2[1] = int(t2[1]) + 1
    r1 = list(range(*t1))
    r2 = list(range(*t2))
    smallest = r1 if len(r1) <= len(r2) else r2
    largest = r1 if len(r1) > len(r2) else r2
    return smallest, largest


def check_full_overlap(r1, r2):
    smallest, largest = format_ranges(r1, r2)
    if smallest[0] >= largest[0] and smallest[-1] <= largest[-1]:
        return 1
    return 0


def check_overlap(r1, r2):
    smallest, largest = format_ranges(r1, r2)
    for num in smallest:
        if num in largest:
            return 1
    return 0


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        full = 0
        partial = 0
        for pair in f:
            full += check_full_overlap(*pair.split(","))
            partial += check_overlap(*pair.split(","))

        print("Number of full overlaps:", full)
        print("Number of partial overlaps:", partial)
