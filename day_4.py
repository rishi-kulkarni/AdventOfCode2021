import csv


def part_1_helper(sequence, board_list):
    winning_board = []
    for value in sequence:
        for idx, board in enumerate(board_list):
            board_list[idx] = [[0 if x == value else x for x in row] for row in board]
            for row in board_list[idx]:
                if any(row) is False:
                    winning_board = idx
                    break
            for column in zip(*board_list[idx]):
                if any(column) is False:
                    winning_board = idx
                    break
            if isinstance(winning_board, int):
                break
        if isinstance(winning_board, int):
            break

    total = 0
    for row in board_list[winning_board]:
        total += sum(row)

    return total * value


def part_2_helper(sequence, board_list):
    total_boards = len(board_list)
    boards_that_have_won = [0 for x in range(total_boards)]
    for value in sequence:
        for idx, board in enumerate(board_list):
            board_list[idx] = [[0 if x == value else x for x in row] for row in board]
            for row in board_list[idx]:
                if any(row) is False:
                    boards_that_have_won[idx] = 1
                    break
            for column in zip(*board_list[idx]):
                if any(column) is False:
                    boards_that_have_won[idx] = 1
                    break
            if sum(boards_that_have_won) == total_boards:
                break
        if sum(boards_that_have_won) == total_boards:
            break

    total = 0
    for row in board_list[idx]:
        total += sum(row)

    return total * value


if __name__ == "__main__":

    input = []
    sequence = []
    board_list = []
    with open("day_4_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", skipinitialspace=True)
        current_board = []
        for idx, row in enumerate(reader):

            if idx == 0:
                sequence = row[0].split(",")
                sequence = [int(x) for x in sequence]

            elif len(row) == 5:
                current_board.append([int(x) for x in row])

            elif len(row) == 0 and len(current_board) > 0:
                board_list.append(current_board)
                current_board = []
        board_list.append(current_board)

    print(f"The answer to part 1 is {part_1_helper(sequence, board_list)}")
    print(f"The answer to part 1 is {part_2_helper(sequence, board_list)}")
