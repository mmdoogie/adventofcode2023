from collections import defaultdict
from itertools import combinations, pairwise

from mrm.djikstra import djikstra

with open('data/aoc-2023-25.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def parse():
    edges = defaultdict(set)
    for d in dat:
        l, r = d.split(': ')
        r = r.split(' ')
        for rr in r:
            edges[l].add(rr)
            edges[rr].add(l)
    return edges

def part1(output = True):
    crossings = defaultdict(lambda: 0)

    edges = parse()
    psp = None
    for e1, e2 in combinations(edges, 2):
        if psp != e1:
            w, p = djikstra(edges, start_point=e1)
            psp = e1
        for pp in pairwise(p[e2]):
            crossings[pp] += 1

    imp_nodes = sorted(crossings.items(), key=lambda x:x[1], reverse=True)[:6]

    for i in imp_nodes:
        edges[i[0][0]].remove(i[0][1])

    w1, w2 = 0, 0
    for e in edges:
        w = djikstra(edges, start_point=e, keep_paths=False)
        if w1 == 0:
            w1 = len(w)
        if len(w) == w1:
            continue
        w2 = len(w)
        break

    return w1 * w2

def part2(output = True):
    return 'Snowverload!'

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
