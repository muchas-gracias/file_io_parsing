
with open("textfiles/parsing1.txt", "r") as file:
    lines = file.readlines()

lists = [line.strip().split(", ") for line in lines]

print(lists)
