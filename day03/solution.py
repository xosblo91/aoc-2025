def main():
    data = read()
    sol1(data)
    sol2(data)


def sol1(data):
    sum_joltage = 0

    for row in data:
        sum_joltage += int(optimize_v1(row))

    print(sum_joltage)


def sol2(data):
    sum_joltage = 0

    for row in data:
        sum_joltage += int(optimize_v2(row, 12))

    print(sum_joltage)


def optimize_v1(row):
    highest_str = 0
    for index, battery in enumerate(row):
        for i in range(index, len(row)):
            if index == i:
                continue
            temp_str = str(battery) + str(row[i])
            if int(temp_str) > int(highest_str):
                highest_str = temp_str

    return highest_str


def optimize_v2(row, battery_count):
    result = []
    deletions_allowed = len(row) - battery_count

    for battery in row:
        while len(result) > 0 and battery > result[-1] and deletions_allowed > 0:
            result.pop()
            deletions_allowed -= 1

        result.append(battery)

    return "".join(map(str, result[:battery_count]))


def read():
    data = []

    with open("input.txt", "r") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                row_of_ints = [int(char) for char in clean_line]
                data.append(row_of_ints)

    return data


if __name__ == "__main__":
    main()
