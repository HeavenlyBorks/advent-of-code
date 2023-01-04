import sys


class Stack:
    def __init__(self, d: "list[list[int]]"):
        self.stacks = d

    def move(self, q, f, t):
        for i in range(q - 1, -1, -1):
            try:
                self.stacks[t - 1].append(self.stacks[f - 1].pop(-1 - i))
            except IndexError:
                print(f"No more to move from {f}")


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        stack = Stack(
            [
                ["c", "z", "n", "b", "m", "w", "q", "v"],
                ["h", "z", "r", "w", "c", "b"],
                ["f", "q", "r", "j"],
                ["z", "s", "w", "h", "f", "n", "m", "t"],
                ["g", "f", "w", "l", "n", "q", "p"],
                ["l", "p", "w"],
                ["v", "b", "d", "r", "g", "c", "q", "j"],
                ["z", "q", "n", "b", "w"],
                ["h", "l", "f", "c", "g", "t", "j"],
            ]
        )

        for line in f:
            line = line.split()
            stack.move(int(line[1]), int(line[3]), int(line[5]))

        for s in stack.stacks:
            print(s[-1])
