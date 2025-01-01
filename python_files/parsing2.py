
with open("textfiles/parsing1.txt", "r") as file:
    lines = file.readlines()


flat_list = [int(num) for line in lines for num in line.strip().split(", ")]


print(flat_list)
