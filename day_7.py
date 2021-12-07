import csv


def solver_1(positions):
    positions.sort()  # median minimizes absolute loss
    mid = int(len(positions) / 2)
    median = sum((positions[mid], positions[mid - 1])) / 2  # even number
    sum_fuel = 0
    for x in positions:
        sum_fuel += abs(median - x)
    return sum_fuel


def solver_2(positions):
    line_space = [x for x in range(1, max(positions) + 1)]
    loss = [0 for x in line_space]
    for idx, v in enumerate(line_space):
        for v_2 in positions:
            distance = abs(v - v_2)
            loss[idx] += (distance * (distance + 1)) / 2
    return min(loss)


if __name__ == "__main__":
    positions = []
    with open("day_7_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", skipinitialspace=True)
        positions = list(map(int, next(reader)))

    print(f"The answer to part 1 is {solver_1(positions)}")
    print(f"The answer to part 2 is {solver_2(positions)}")
