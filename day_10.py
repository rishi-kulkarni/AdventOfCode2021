import csv

mapping_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def solver_1(chunks):
    score = 0
    for row in chunks:
        stack = []
        for token in row:
            if token in mapping_dict.keys():
                stack.insert(0, token)
            elif mapping_dict[stack[0]] == token:
                stack.pop(0)
            else:
                score += scores[token]
                break
    return score


def solver_2(chunks):
    score_list = []
    for row in chunks:
        stack = []
        for token in row:
            if token in mapping_dict.keys():
                stack.insert(0, token)
            elif mapping_dict[stack[0]] == token:
                stack.pop(0)
            else:
                break
        else:
            autocomplete = [mapping_dict[x] for x in stack]
            score = 0
            for element in autocomplete:
                score *= 5
                score += scores_2[element]
            score_list.append(score)
    score_list.sort()
    return score_list[int(len(score_list) / 2)]


if __name__ == "__main__":
    with open("day_10_input.txt") as csvfile:
        chunks = []
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            chunks.append(list(row[0]))

    print(f"The answer to part 1 is {solver_1(chunks)}")
    print(f"The answer to part 2 is {solver_2(chunks)}")
