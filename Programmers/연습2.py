def print_table(table):
    for row in table:
        for col in row:
            print(str(col) + ' ', end='')
        print()


DIR = [(1, 0), (0, 1), (-1, -1)]
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR = {
    'EAST': (0, 1),
    'WEST': (0, -1),
    'SOUTH': (-1, 0),
    'NORTH': (1, 0)
}

current_dir = DIR['NORTH']

input = 6
dir_idx = 0

table = [[0 for i in range(input)] for j in range(input)]
print_table(table)

print("-----------")

location = (-1, 0)
number = 1

for step in range(input, 0, -1):
    current_dir = DIR[dir_idx]

    for _ in range(step):
        y = location[0] + DIR[dir_idx][0]
        x = location[1] + DIR[dir_idx][1]
        table[y][x] = number

        number += 1
        location = (y, x)
    print(current_dir)
    dir_idx = (dir_idx + 1) % 3

print("-----------")
print_table(table)
