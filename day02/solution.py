import re


def main():
    data = read()
    sol1(data)
    sol2(data)


def sol1(data):
    result = str(solver(data, r"^(\d+)\1$"))
    print(f"Solution 1: {result}")


def sol2(data):
    result = str(solver(data, r"^(\d+)\1+$"))
    print(f"Solution 2: {result}")


def solver(data, exp):
    invalid = 0

    for start, end in data:
        for number in range(start, end + 1):
            if bool(re.match(exp, str(number))):
                invalid += number

    return invalid


def read():
    with open("input.txt", "r") as f:
        data = f.read()

    range_strings = [s.strip() for s in data.split(",") if s.strip()]

    result_list = []
    for range_str in range_strings:
        start_str, end_str = range_str.split("-")
        start = int(start_str.strip())
        end = int(end_str.strip())
        result_list.append((start, end))

    return result_list


if __name__ == "__main__":
    main()
