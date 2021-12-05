import csv


def solver(coordinate_list):
    table = [[0 for c in range(1000)] for r in range(1000)]

    for row in coordinate_list:
        dx = -1 if (row[1][0] - row[0][0]) < 0 else (1 if (row[1][0] - row[0][0]) > 0 else 0)
        dy = -1 if (row[1][1] - row[0][1]) < 0 else (1 if (row[1][1] - row[0][1]) > 0 else 0)
        write_x, write_y = row[0]
        end_x, end_y = row[1]

        while (write_x != end_x + dx) or (write_y != end_y + dy):
            table[write_y][write_x] += 1
            write_x += dx
            write_y += dy

    danger_spots = 0
    for row in table:
        danger_spots += sum(1 for x in row if x > 1)

    return danger_spots


if __name__ == "__main__":

    coordinate_list = []

    with open("day_5_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)

        for row in reader:
            append = [list(map(int, x.split(","))) for x in row if x != "->"]
            coordinate_list.append(append)

    h_v_only = [x for x in coordinate_list if x[0][0] == x[1][0] or x[0][1] == x[1][1]]

    print(f"The answer to part 1 is {solver(h_v_only)}")
    print(f"The answer to part 2 is {solver(coordinate_list)}")
