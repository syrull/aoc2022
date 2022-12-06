def import_input():
    string = None
    with open("../input", "r") as input_file:
        string = input_file.read()
    return string

def parse_input(string: str):
    distinct_chars = 14
    for i in range(0, len(string)):
        uc = set()
        chunk = string[i:i+distinct_chars]
        for s in chunk:
            uc.add(s)
        if len(uc) == distinct_chars:
            return i + distinct_chars

input_ = import_input()
print(parse_input(input_))

