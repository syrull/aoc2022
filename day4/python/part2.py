def import_input():
    lines = []
    with open("../input", "r") as input_file:
        for line in input_file.readlines():
            lines.append(line.replace("\n", ""))
    return lines


def split_sections(sections_string: str):
    first_section, second_section = sections_string.split(",")
    first_section_range = [int(i) for i in first_section.split("-")]
    second_section_range = [int(i) for i in second_section.split("-")]
    first_section_range_gen = [i for i in range(first_section_range[0], first_section_range[1] + 1)]
    second_section_range_gen = [i for i in range(second_section_range[0], second_section_range[1] + 1)]

    for n in first_section_range_gen:
        if n in second_section_range_gen:
            return True 


input_ = import_input()
res = 0
for l in input_:
    if split_sections(l):
        res += 1
print(res)

