def main():
    instructions = read()
    sol1(instructions)
    sol2(instructions)


def sol1(instructions):
    dial = 50
    total = 0

    for direction, steps in instructions:
        dial, _ = move(dial, steps, direction)
        if dial == 0:
            total += 1

    print(total)


def sol2(instructions):
    dial = 50
    total = 0

    for direction, steps in instructions:
        dial, z = move(dial, steps, direction)
        total += z

    print(total)


def move(start, steps, direction):
    out = start
    zero_count = 0

    step = 1 if direction == "R" else -1

    for _ in range(steps):
        out += step
        if out == 100:
            out = 0
        elif out == -1:
            out = 99
        if out == 0:
            zero_count += 1

    return out, zero_count


def read():
    with open("input.txt", "r") as file:
        instructions = [line.strip() for line in file if line.strip()]
    return [(line[0], int(line[1:])) for line in instructions]


if __name__ == "__main__":
    main()
