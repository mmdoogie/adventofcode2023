from math import log10, ceil

import ansi_term as ansi

with open('data/aoc-2023-05.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def apply_maps(maps, seed):
    pre_map = seed
    for m in maps:
        for ds, ss, rl in m:
            if ss <= pre_map < ss + rl:
                pre_map = ds + (pre_map - ss)
                break
    return pre_map

def parse(seed_ranges = False):
    seeds = [int(x) for x in dat[0].split(': ')[1].split(' ')]

    if seed_ranges:
        seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    maps = []
    curr_map = []
    for d in dat[3:]:
        if d == '':
            continue
        if ':' in d:
            maps += [curr_map]
            curr_map = []
        else:
            curr_map += [tuple(int(x) for x in d.split(' '))]

    maps += [curr_map]

    return seeds, maps

def part1(output = True):
    seeds, maps = parse(seed_ranges = False)
    locs = {apply_maps(maps, s): s for s in seeds}
    min_loc = min(locs.keys())

    if output:
        for lk, lv in locs.items():
            if lk == min_loc:
                print(ansi.COLOR_GREEN, end='')
            print(f'Seed {lv:<10d} maps to location {lk}')
            if lk == min_loc:
                print(ansi.TEXT_RESET, end='')

    return min_loc

def part2(output = True):
    seeds, maps = parse(seed_ranges = True)

    step_size = int(pow(10, ceil(log10(max(s[1] for s in seeds) / 100))))
    search_vals = {(ss, ss + sl, s): apply_maps(maps, s) for ss, sl in seeds for s in range(ss, ss + sl, step_size)}
    rough_est = min(search_vals.items(), key = lambda x: x[1])

    seed_range_start, seed_range_end, best_est = rough_est[0]

    if output:
        print(f'Best estimate: {best_est} in seed range {seed_range_start} to {seed_range_end}')
        print(f'Step size: {step_size:<8d}, best estimate: {best_est:<10d} near loc {rough_est[1]}')

    while step_size > 1:
        left_search  = max(best_est - step_size, seed_range_start)
        right_search = min(best_est + step_size, seed_range_end)

        step_size = step_size // 10
        search_vals = {s: apply_maps(maps, s) for s in range(left_search, right_search, step_size)}
        best_est, best_loc = min(search_vals.items(), key = lambda x: x[1])

        if output:
            print(f'Step size: {step_size:<8d}, best estimate: {best_est:<10d} near loc {best_loc}')

    return best_loc

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
