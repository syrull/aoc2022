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

    if first_section_range[0] <= second_section_range[0] and first_section_range[1] >= second_section_range[1]:
        return True

    if second_section_range[0] <= first_section_range[0] and second_section_range[1] >= first_section_range[1]:
        return True

    if first_section_range[0] == first_section_range[1]:
        return ((first_section_range[0] == second_section_range[1]) or (first_section_range[0] == second_section_range[0]))

    if second_section_range[0] == second_section_range[1]:
        return ((second_section_range[0] == first_section_range[1]) or (second_section_range[0] == first_section_range[0]))

   
input_ = import_input()
res = 0
for l in input_:
    if split_sections(l):
        res += 1
print(res)

