def main():
    ranges, numbers = read()
    sol1(ranges, numbers)
    sol2(ranges)


def sol1(ranges, numbers):
    fresh = 0
    for i in numbers:
        for lower, upper in ranges:
            if lower <= i <= upper:
                fresh += 1
                break

    print(fresh)


def sol2(ranges):
    ranges.sort()

    merged = []
    lower, upper = ranges[0]

    index = 0
    for current_lower, current_upper in ranges:
        if index == 0:
            index += 1
            continue
        if current_lower <= upper + 1:
            upper = max(upper, current_upper)
        else:
            merged.append((lower, upper))
            lower, upper = current_lower, current_upper

    merged.append((lower, upper))

    fresh = 0
    for current_lower, current_upper in merged:
        fresh += current_upper - current_lower + 1

    print(fresh)


def read():
    ranges = []
    numbers = []

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if "-" in line:
                start, end = line.split("-")
                ranges.append((int(start), int(end)))
            else:
                numbers.append(int(line))

    return ranges, numbers


if __name__ == "__main__":
    main()
