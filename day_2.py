import csv
from typing import Match

def question_one_helper(input):
    horizontal, depth = 0, 0
    for row in input:
        direction=row[0]
        distance=int(row[1])
        match direction:
            case 'forward': horizontal += distance
            case 'down': depth += distance
            case 'up': depth -= distance

    return horizontal * depth

def question_two_helper(input):
    horizontal, depth, aim = 0, 0, 0
    for row in input:
        direction=row[0]
        distance=int(row[1])
        match direction:
            case 'forward': 
                horizontal += distance
                depth += distance*aim
            case 'down': aim += distance
            case 'up': aim -= distance

    return horizontal * depth    

if __name__ == "__main__":

    input = []

    with open("day_2_input.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            input.append(row)

    print(f"The solution to part one is {question_one_helper(input)}")
    print(f"The solution to part one is {question_two_helper(input)}")