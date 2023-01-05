import sys


if __name__ == "__main__":
    l = open(sys.argv[0]).read().strip()
    for i in range(3, len(l)):
        for letter in l[i - 4 : i + 1]:
            pass
