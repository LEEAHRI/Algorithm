def print_table(table):
    for row in table:
        for col in row:
            print(str(col) + ' ', end='')
        print()


DIR = [(1, 0), (0, 1), (-1, -1)]

input = 6
dir_idx = 0

table = [[0 for i in range(input)] for j in range(input)]
print_table(table)

for step in range(input, 0, -1):
    current_dir = DIR[dir_idx]
    print(current_dir)
    dir_idx = (dir_idx + 1) % 3
