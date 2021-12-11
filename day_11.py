import csv

legal_directions = (
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)


def solver_1(input, steps):
    grid = [[i for i in row] for row in input]
    flashes = 0
    for step in range(steps):
        stack = []
        for x_val, row in enumerate(grid):
            for y_val, element in enumerate(row):
                if element < 9:
                    grid[x_val][y_val] += 1
                else:
                    stack.append(tuple((x_val, y_val)))
                    grid[x_val][y_val] = 0
                    flashes += 1
        while stack:
            x, y = stack.pop(0)
            for x_plus, y_plus in legal_directions:
                target_x, target_y = x + x_plus, y + y_plus
                if target_x < 0 or target_x >= len(grid):
                    pass
                elif target_y < 0 or target_y >= len(grid[0]):
                    pass
                elif grid[target_x][target_y] == 0:
                    pass
                elif grid[target_x][target_y] < 9:
                    grid[target_x][target_y] += 1
                elif grid[target_x][target_y] == 9:
                    stack.append(tuple((target_x, target_y)))
                    grid[target_x][target_y] = 0
                    flashes += 1
    return flashes


def solver_2(input):
    grid = [[i for i in row] for row in input]
    step = 0
    while True:
        step += 1
        stack = []
        for x_val, row in enumerate(grid):
            for y_val, element in enumerate(row):
                if element < 9:
                    grid[x_val][y_val] += 1
                else:
                    stack.append(tuple((x_val, y_val)))
                    grid[x_val][y_val] = 0
        while stack:
            x, y = stack.pop(0)
            for x_plus, y_plus in legal_directions:
                target_x, target_y = x + x_plus, y + y_plus
                if target_x < 0 or target_x >= len(grid):
                    pass
                elif target_y < 0 or target_y >= len(grid[0]):
                    pass
                elif grid[target_x][target_y] == 0:
                    pass
                elif grid[target_x][target_y] < 9:
                    grid[target_x][target_y] += 1
                elif grid[target_x][target_y] == 9:
                    stack.append(tuple((target_x, target_y)))
                    grid[target_x][target_y] = 0

        if sum([sum(row) for row in grid]) == 0:
            return step


if __name__ == "__main__":

    with open("day_11_input.txt") as csvfile:
        test_grid = []
        reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)
        for row in csvfile:
            test_grid.append([int(x) for x in list(row.strip())])

    print(f"The answer to part 1 is {solver_1(test_grid, 100)}")
    print(f"The answer to part 2 is {solver_2(test_grid)}")
