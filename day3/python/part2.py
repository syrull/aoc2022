import string


alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def import_input():
    lines = []
    with open("../input", "r") as input_file:
        for line in input_file.readlines():
            lines.append(line.replace("\n", ""))
    return lines


def calculate_score(letter) -> int:
    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            return i + 1


task_input = import_input()
sum_score = 0
chunks = []
chunk_size = 3

for i in range(0, len(task_input), chunk_size):
    batch = task_input[i:i+chunk_size]
    letters = list(batch[0])
    unique_letter = None

    for letter in letters:
        if letter in batch[1] and letter in batch[2]:
            unique_letter = letter
            break
    sum_score += calculate_score(unique_letter)

print(sum_score)