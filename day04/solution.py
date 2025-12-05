def main():
    data = read()
    sol1(data)


def sol1(grid):
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
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
