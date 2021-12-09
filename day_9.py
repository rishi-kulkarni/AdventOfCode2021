import csv


def basin_filler(idx_row, idx_column, cave_map):
    basin_size = 1
    indices = set((tuple((idx_row, idx_column)),))
    while True:
        new_indices = set()
        for i_row, i_column in indices:
            if i_row > 0 and cave_map[i_row - 1][i_column] != 9:
                new_indices.add(tuple((i_row - 1, i_column)))
            if i_row < len(cave_map) - 1 and cave_map[i_row + 1][i_column] != 9:
                new_indices.add(tuple((i_row + 1, i_column)))
            if i_column > 0 and cave_map[i_row][i_column - 1] != 9:
                new_indices.add(tuple((i_row, i_column - 1)))
            if i_column < len(cave_map[0]) - 1 and cave_map[i_row][i_column + 1] != 9:
                new_indices.add(tuple((i_row, i_column + 1)))
        if len(new_indices.union(indices)) == len(indices):
            break
        else:
            indices = new_indices.union(indices)

    basin_size = len(indices)

    return basin_size


def solver_1(cave_map):
    sum_of_risks = 0

    for idx_row, row in enumerate(cave_map):
        for idx_column, element in enumerate(row):
            current_status = 0
            if idx_row > 0:
                current_status += element >= cave_map[idx_row - 1][idx_column]
            if idx_row < len(cave_map) - 1:
                current_status += element >= cave_map[idx_row + 1][idx_column]
            if idx_column > 0:
                current_status += element >= cave_map[idx_row][idx_column - 1]
            if idx_column < len(row) - 1:
                current_status += element >= cave_map[idx_row][idx_column + 1]

            if current_status == 0:
                sum_of_risks += element + 1
    return sum_of_risks


def solver_2(cave_map):
    basins = []

    for idx_row, row in enumerate(cave_map):
        for idx_column, element in enumerate(row):
            current_status = 0
            if idx_row > 0:
                current_status += element >= cave_map[idx_row - 1][idx_column]
            if idx_row < len(cave_map) - 1:
                current_status += element >= cave_map[idx_row + 1][idx_column]
            if idx_column > 0:
                current_status += element >= cave_map[idx_row][idx_column - 1]
            if idx_column < len(row) - 1:
                current_status += element >= cave_map[idx_row][idx_column + 1]

            if current_status == 0:
                basins.append(basin_filler(idx_row, idx_column, cave_map))

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == "__main__":

    with open("day_9_input.txt") as csvfile:
        cave_map = []
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            cave_map.append([int(x) for x in list(row[0])])

    print(f"The answer to part 1 is {solver_1(cave_map)}")
    print(f"The answer to part 2 is {solver_2(cave_map)}")
