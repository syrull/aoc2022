import string


alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def import_input():
    lines = []
    with open("../input", "r") as input_file:
        for line in input_file.readlines():
            lines.append(line.replace("\n", ""))
    return lines


def split_string(string_: str) -> str:
    return string_[:len(string_) // 2], string_[len(string_) // 2:]


def calculate_score(letters: list) -> int:
    score = 0
    for i in range(len(alphabet)):
        if alphabet[i] in letters:
            score += i + 1
    return score


task_input = import_input()
score = 0

for string_ in task_input:
    unique_letters = list()
    first, second = split_string(string_)
    for letter in first:
        if letter in second:
            unique_letters.append(letter)
            break
    score += calculate_score(unique_letters)

print(score)