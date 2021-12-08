import csv


def find_mapping(row):
    mapping_list = [0 for i in range(10)]
    mapping_list[1] = [x for x in row if len(x) == 2][0]
    mapping_list[7] = [x for x in row if len(x) == 3][0]
    mapping_list[4] = [x for x in row if len(x) == 4][0]
    mapping_list[8] = [x for x in row if len(x) == 7][0]

    nine_finder = set(mapping_list[4]).union(set(mapping_list[7]))
    mapping_list[9] = [x for x in row if nine_finder.issubset(x) and len(x) == 6][0]

    two_finder = set(mapping_list[8]) - set(mapping_list[9])
    mapping_list[2] = [x for x in row if two_finder.issubset(x) and len(x) == 5][0]

    five_finder = set(mapping_list[8]) - set(mapping_list[2])
    mapping_list[5] = [x for x in row if five_finder.issubset(x) and len(x) == 5][0]

    three_finder = (
        set(mapping_list[2])
        .intersection(set(mapping_list[5]))
        .union(set(mapping_list[1]))
    )
    mapping_list[3] = [x for x in row if three_finder.issubset(x) and len(x) == 5][0]

    zero_finder = (
        set(mapping_list[2])
        .intersection(set(mapping_list[5]))
        .intersection(set(mapping_list[4]))
    )
    mapping_list[0] = [x for x in row if not zero_finder.issubset(x) and len(x) == 6][0]

    six_finder = two_finder.union(set(mapping_list[5]))
    mapping_list[6] = [x for x in row if six_finder.issubset(x) and len(x) == 6][0]

    return mapping_list


def solver_1(inputs, outputs):

    instances = 0
    for idx, row in enumerate(inputs):
        mapping_list = find_mapping(row)

        for output in outputs[idx]:
            if sorted(output) in (
                sorted(mapping_list[1]),
                sorted(mapping_list[4]),
                sorted(mapping_list[7]),
                sorted(mapping_list[8]),
            ):
                instances += 1

    return instances


def solver_2(inputs, outputs):

    total = 0

    for idx, row in enumerate(inputs):
        mapping_list = find_mapping(row)
        mapping_list = [sorted(x) for x in mapping_list]
        digits = []

        for output in outputs[idx]:
            digits.append(str(mapping_list.index(sorted(output))))

        total += int("".join(digits))

    return total


if __name__ == "__main__":

    with open("day_8_input.txt") as csvfile:
        inputs = []
        outputs = []
        reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)
        for row in reader:
            input, output = row[: row.index("|")], row[(row.index("|") + 1) :]
            inputs.append(input)
            outputs.append(output)

    print(f"The answer to part 1 is {solver_1(inputs, outputs)}")
    print(f"The answer to part 2 is {solver_2(inputs, outputs)}")
