import sys


def is_max(num, array):
    for n in array:
        if n >= num:
            print(f"{array} - {num} not max")
            return False
    print(f"{array} - {num} max")
    return True


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        grid = []
        for line in f:
            grid.append(line.strip())

    def total_viewed_trees():
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (
                    is_max(grid[row][column], grid[row][:column])
                    or is_max(grid[row][column], grid[row][column + 1 :])
                    or is_max(
                        grid[row][column], [grid[y][column] for y in range(0, row)]
                    )
                    or is_max(
                        grid[row][column],
                        [grid[y][column] for y in range(row + 1, len(grid))],
                    )
                ):
                    count += 1

        print(count)

    def highest_scenic_score():
        max_scenic = 0
        indexes = [0, 0]
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                match = grid[row][column]
                total = 1
                temp = 0
                # up
                for i in range(row - 1, -1, -1):
                    temp += 1
                    if grid[i][column] >= match:
                        break
                total *= temp
                temp = 0
                # left
                for i in range(column - 1, -1, -1):
                    temp += 1
                    if grid[row][i] >= match:
                        break
                total *= temp
                temp = 0
                # right
                for i in range(column + 1, len(grid[row])):
                    temp += 1
                    if grid[row][i] >= match:
                        break
                total *= temp
                temp = 0
                # down
                for i in range(row + 1, len(grid)):
                    temp += 1
                    if grid[i][column] >= match:
                        break
                total *= temp
                if total > max_scenic:
                    max_scenic = total
                    indexes = [row, column]

        print(max_scenic, indexes)
