dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def rotate(rc, rotate_stack):
    border = []
    width, height = len(rc[0]), len(rc)
    dir_idx = 0
    y, x = 0, 0
    while True:
        border.append(rc[y][x])
        if not (0 <= y + dir[dir_idx][0] < height and 0 <= x + dir[dir_idx][1] < width):
            dir_idx += 1
        if dir_idx == 4:
            break
        y += dir[dir_idx][0]
        x += dir[dir_idx][1]
    del border[len(border) - 1]

    new_border = border[len(border) - rotate_stack:] + border[:len(border) - rotate_stack]
    dir_idx = 0
    y, x = 0, 0
    for item in new_border:
        rc[y][x] = item
        if not (0 <= y + dir[dir_idx][0] < height and 0 <= x + dir[dir_idx][1] < width):
            dir_idx += 1
        y += dir[dir_idx][0]
        x += dir[dir_idx][1]


def solution(rc, operations):
    rotate_stack, shift_stack = 0, 0
    border_size = len(rc) * 2 + len(rc[0]) * 2 - 4
    for op in operations:
        if op == 'ShiftRow':
            if rotate_stack > 0:
                rotate_stack %= border_size
                rotate(rc, rotate_stack)
                rotate_stack = 0
            shift_stack += 1
        if op == 'Rotate':
            if shift_stack > 0:
                shift_stack %= len(rc)
                rc = rc[len(rc) - shift_stack:] + rc[:len(rc) - shift_stack]
                shift_stack = 0
            rotate_stack += 1

    if rotate_stack > 0:
        rotate_stack %= border_size
        rotate(rc, rotate_stack)
    if shift_stack > 0:
        shift_stack %= len(rc)
        rc = rc[len(rc) - shift_stack:] + rc[:len(rc) - shift_stack]
    return rc