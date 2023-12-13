with open('data/aoc-2023-13.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def grids():
    blank_lines = [i for i, d in enumerate(dat) if d == ''] + [len(dat)]
    start = 0
    for b in blank_lines:
        yield dat[start:b]
        start = b + 1

def is_mirrored(grid, row, smudged = False):
    i, j = row, row + 1
    fixed = False
    while i >= 0 and j < len(grid):
        if grid[i] != grid[j] and i != row:
            if not smudged:
                return False
            diff_cnt = sum(a != b for a, b in zip(grid[i], grid[j]))
            if diff_cnt != 1 or fixed:
                return False
            fixed = True
        i -= 1
        j += 1
    return fixed or not smudged

def transpose(grid):
    res = []
    for x in range(len(grid[0])):
        row = ''
        for y in range(len(grid)):
            row += grid[y][x]
        res += [row]
    return res

def summarize(grid, smudged = False):
    matched = [i for i, g_1 in enumerate(grid)
                 for j, g_2 in enumerate(grid)
                 if i != j and g_1 == g_2 and j - i == 1]
    for m in matched:
        if is_mirrored(grid, m, smudged = smudged):
            return 100 * (m + 1)

    if smudged:
        matched = [i for i, g_1 in enumerate(grid)
                     for j, g_2 in enumerate(grid)
                     if i != j and sum(a != b for a, b in zip(g_1, g_2)) == 1 and j - i == 1]
        for m in matched:
            if is_mirrored(grid, m, smudged = False):
                return 100 * (m + 1)

    t_grid = transpose(grid)

    matched = [i for i, g_1 in enumerate(t_grid)
                 for j, g_2 in enumerate(t_grid)
                 if i != j and g_1 == g_2 and j - i == 1]
    for m in matched:
        if is_mirrored(t_grid, m, smudged = smudged):
            return m + 1

    if smudged:
        matched = [i for i, g_1 in enumerate(t_grid)
                     for j, g_2 in enumerate(t_grid)
                     if i != j and sum(a != b for a, b in zip(g_1, g_2)) == 1 and j - i == 1]
        for m in matched:
            if is_mirrored(t_grid, m, smudged = False):
                return m + 1

    assert False
    return 0

def part1(output = True):
    return sum(summarize(g, smudged = False) for g in grids())

def part2(output = True):
    return sum(summarize(g, smudged = True) for g in grids())

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
