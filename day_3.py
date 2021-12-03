import csv


def part_1_helper(input):
    target = len(input) / 2
    counter = [sum(list(map(int, column))) for column in zip(*input)]
    gamma = int("".join([str(1) if x > target else str(0) for x in counter]), 2)
    epsilon = int("".join([str(0) if x > target else str(1) for x in counter]), 2)
    return gamma * epsilon


def part_2_helper(input):
    o2_candidates = input.copy()
    co2_candidates = input.copy()
    for i, _ in enumerate(input[0]):
        target = len(o2_candidates) / 2
        counter = [sum(list(map(int, column))) for column in zip(*o2_candidates)]
        if counter[i] >= target:
            o2_candidates = [x for x in o2_candidates if x[i] == "1"]
        else:
            o2_candidates = [x for x in o2_candidates if x[i] == "0"]

        if len(o2_candidates) == 1:
            break

    for i, _ in enumerate(input[0]):

        target = len(co2_candidates) / 2
        counter = [sum(list(map(int, column))) for column in zip(*co2_candidates)]
        if counter[i] >= target:
            co2_candidates = [x for x in co2_candidates if x[i] == "0"]
        else:
            co2_candidates = [x for x in co2_candidates if x[i] == "1"]
        if len(co2_candidates) == 1:
            break

    return int(o2_candidates[0], 2) * int(co2_candidates[0], 2)


if __name__ == "__main__":

    input = []

    with open("day_3_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            input.append(row[0])

    print(f"The answer to part 1 is {part_1_helper(input)}")
    print(f"The answer to part 2 is {part_2_helper(input)}")
