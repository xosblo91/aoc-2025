def main():
    data = read()
    sol1(data)


def sol1(data):
    sum_joltage = 0

    for row in data:
        sum_joltage += int(optimize(row))

    print(sum_joltage)

def optimize(row):
    highest = 0
    highest_str=0
    for index,battery in enumerate(row):
        for i in range(index,len(row)):
            if index == i:
                continue
            temp_str = str(battery) + str(row[i])
            if int(temp_str) > int(highest_str):
                highest_str = temp_str

    return highest_str

def read():
    data_2d_int=[]

    with open("sample.txt", 'r') as f:
        for line in f:
            clean_line = line.strip()
            if clean_line: # Ensure we don't process empty lines
                row_of_ints = [int(char) for char in clean_line]
                data_2d_int.append(row_of_ints)

    return data_2d_int

if __name__ == "__main__":
    main()
