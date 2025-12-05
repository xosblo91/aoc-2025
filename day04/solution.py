def main():
    data = read()
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    sol1(data, adjacent)
    sol2(data, adjacent)


def sol1(grid, adjacent):
    accessible = 0

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col != "@":
                continue
            count = 0
            for ax, ay in adjacent:
                if 0 <= x + ax < len(grid) and 0 <= y + ay < len(row):
                    if grid[x + ax][y + ay] == "@":
                        count += 1

            if count < 4:
                accessible += 1

    print(accessible)


def sol2(grid, adjacent):
    removed = 0

    keep_removing = True
    while keep_removing:
        grid, keep_removing = remover(grid, adjacent)
        if keep_removing:
            removed += 1

    print(removed)


def remover(grid, adjacent):
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col != "@":
                continue
            count = 0
            for ax, ay in adjacent:
                if 0 <= x + ax < len(grid) and 0 <= y + ay < len(row):
                    if grid[x + ax][y + ay] == "@":
                        count += 1

            if count < 4:
                grid[x][y] = "."
                return grid, True

    return grid, False


def read():
    data = []

    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            if row:
                data.append(row)
    return data


if __name__ == "__main__":
    main()
