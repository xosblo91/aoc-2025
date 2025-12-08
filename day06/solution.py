import math


def main():
    data = read()
    sol1(data)


def sol1(data):
    total = 0
    for row in data:
        local_total = 0
        if row.get("op") == "*":
            local_total = math.prod(row.get("values"))
        elif row.get("op") == "+":
            local_total = sum(row.get("values"))

        total += local_total

    print(total)


def read():
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f if line.strip()]

    ops = lines[-1].split()
    numbers = lines[:-1]

    columns = []
    for line in numbers:
        nums = line.split()
        for i, n in enumerate(nums):
            if len(columns) <= i:
                columns.append([])
            columns[i].append(int(n))

    data = []
    for i, column_values in enumerate(columns):
        data.append({
            "op": ops[i],
            "values": column_values
        })

    return data


if __name__ == "__main__":
    main()
