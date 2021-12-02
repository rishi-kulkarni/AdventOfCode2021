import csv


def compare_function(input, distance=1):
    total_increasing = 0
    iterable = input[distance:]
    increasing_indexes = [idx for idx, v in enumerate(iterable) if v > input[idx]]
    return len(increasing_indexes)


if __name__ == "__main__":

    input = []

    with open("day_1_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            input.append(int(row[0]))

    print(f"The answer to question 1 is {compare_function(input)}")

    print(f"The answer to question 2 is {compare_function(input, 3)}")
