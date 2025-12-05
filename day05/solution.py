def main():
    ranges, numbers = read()
    sol1(ranges, numbers)
    sol2(ranges, numbers)


def sol1(ranges, numbers):
    good = 0
    for i in numbers:
        for lower, upper in ranges:
            if i >= lower and i <= upper:
                #print(str(i) + " " + str(lower) + " " + str(upper))
                good += 1
                break

    print(good)

# python ba dör
def sol2(ranges, numbers):
    # dic={}
    # good = 0
    # for lower, upper in ranges:
    #     for i in range(lower,upper+1):
    #         if i not in dic:
    #             dic[i]=i
    #             good +=1   

    # good = set()
    # for lower, upper in ranges:
    #     good.update(range(lower,upper+1))

    # print(len(good))

    # good = {}
    # for lower, upper in ranges:
    #     for i in range(lower, upper + 1):
    #         good[i] = True  # store each number as a key

    print(len(good))


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
