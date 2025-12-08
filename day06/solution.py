import math


def main():
    sol1(read())
    sol2(read2())


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


def sol2(data):
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


def read2():
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f if line.strip()]

    ops = lines[-1].split()
    numbers = lines[:-1]

    columns = []
    for line in numbers:
        for i in range(len(line)):
            if len(columns) <= i:
                columns.append([])
            columns[i].append(line[i])

    result = []
    group = []

    for row in columns:
        if all(x.strip() == "" for x in row):
            if group:
                result.append(group)
                group = []
            continue

        s = ""
        for x in row:
            if x.strip() != "":
                s += x

        if s != "":
            group.append(s)

    if group:
        result.append(group)

    result = [[int(x) for x in grp] for grp in result]

    out = []
    for i, column_values in enumerate(result):
        out.append({
            "op": ops[i],
            "values": column_values
        })

    return out


if __name__ == "__main__":
    main()
