import sys


if __name__ == "__main__":
    l = open(sys.argv[1]).read().strip()
    for i in range(3, len(l)):
        count = 0
        for letter in l[i - 3 : i + 1]:
            count += l[i - 3 : i + 1].count(letter) == 1
        if count == 4:
            print(l[i - 3 : i + 1], i + 1)
            break

    for i in range(13, len(l)):
        count = 0
        for letter in l[i - 13 : i + 1]:
            count += l[i - 13 : i + 1].count(letter) == 1
        if count == 14:
            print(l[i - 13 : i + 1], i + 1)
            break
