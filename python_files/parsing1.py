
with open("../files/parser1.txt", "r") as file:
    lines = file.readlines()

lists = [line.strip().split(", ") for line in lines]

print(lists)
