def import_input():
    lines = []
    with open("../input", "r") as input_file:
        for line in input_file.readlines():
            lines.append(line.replace("\n", ""))
    return lines

    
def parse_movement(input_: str):
    movement = []
    for i in range(len(input_)):
        if input_[i] == "":
            movement = input_[i+1:]
    return movement


def parse_enumeration(input_: str):
    numbers_index = 0
    number_crates = 0
    for i in range(len(input_)):
        if input_[i] == "":
            numbers_index = i - 1
    numbers = [int(i) for i in input_[numbers_index].strip().split("   ")]
    number_crates = numbers[-1]
    return number_crates


def parse_crates(num_crates: int, input_: str):
    list_of_stacks = [list() for _ in range(num_crates)]
    for i in range(len(input_)):
        if input_[i] == "":
            index = i - 1
    splitted_crates = input_[:index]
    for e in splitted_crates:
        stack_value = None
        create_n = 0
        for i in range(0, len(e), 4):
            stack_value = e[i:i+4].strip().replace("[", "").replace("]", "")
            if stack_value:
                list_of_stacks[create_n].append(stack_value)
            create_n += 1
    return list_of_stacks


def move_crates(crates: list[list], movements: list):
    for movement in movements:

        movement = movement.split(" ")
        move = int(movement[1])
        from_ = int(movement[3])
        to = int(movement[5])

        if move == 1:
            value = crates[from_ - 1].pop(0)
            crates[to - 1].insert(0, value)
        else:
            tmp_list = []
            for _ in range(move):
                tmp_list.append(crates[from_ - 1].pop(0))
            for i in tmp_list[::-1]:
                crates[to - 1].insert(0, i)
    return crates


input_ = import_input()
movement = parse_movement(input_)
num_crates = parse_enumeration(input_)
crates = parse_crates(num_crates, input_)
crates = move_crates(crates, movement)
ans = ""
for stack in crates:
    ans += stack.pop(0)
print(ans)