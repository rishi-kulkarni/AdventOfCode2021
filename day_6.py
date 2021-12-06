import csv


def solver(initial_fish_list, days):
    counts = [initial_fish_list.count(x) for x in range(9)]
    for i in range(days):
        counts.append(counts.pop(0))
        counts[6] += counts[8]
    return sum(counts)


if __name__ == "__main__":
    fish_list = []
    with open("day_6_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", skipinitialspace=True)
        fish_list = list(map(int, next(reader)))

        print(f"The answer to part 1 is {solver(fish_list, 80)}")
        print(f"The answer to part 2 is {solver(fish_list, 256)}")
