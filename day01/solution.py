def main():
    instructions = read()
    sol1(instructions)
    sol2(instructions)


def sol1(instructions):
    dial = 50
    zero_count = 0

    for direction, value in instructions:
        if direction == "L":
            dial, _ = left(dial, value)
        else:
            dial, _ = right(dial, value)

        if dial == 0:
            zero_count += 1

    print(dial)
    print(zero_count)


def sol2(instructions):
    dial = 50
    zero_count = 0

    for direction, value in instructions:
        if direction == "L":
            dial, z = left(dial, value)
            zero_count += z
        else:
            dial, z = right(dial, value)
            zero_count += z

    print(dial)
    print(zero_count)


def right(start, count):
    out = start
    zeroCount = 0

    for _ in range(count):
        out += 1
        if out == 100:
            out = 0
        if out == 0:
            zeroCount += 1

    return out, zeroCount


def left(start, count):
    out = start
    zeroCount = 0

    for _ in range(count):
        out -= 1
        if out == -1:
            out = 99
        if out == 0:
            zeroCount += 1

    return out, zeroCount


def read():
    with open("input.txt", "r") as file:
        instructions = [line.strip() for line in file if line.strip()]

    return [(line[0], int(line[1:])) for line in instructions]


if __name__ == "__main__":
    main()
