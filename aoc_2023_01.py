import ansi_term as ansi

with open('data/aoc-2023-01.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def part1(output = True):
    cal_sum = 0
    for d in dat:
        for i1, c1 in enumerate(d):
            if c1 in '0123456789':
                break

        for i2, c2 in enumerate(reversed(d)):
            if c2 in '0123456789':
                break

        cal_sum += int(c1 + c2)
        if output:
            i2 = len(d) - 1 - i2
            print(d[:i1] + ansi.blue(d[i1]) + d[i1 + 1:i2] +
                          (ansi.blue(d[i2]) if i1 != i2 else '') + d[i2 + 1:])

    return cal_sum

def part2(output = True):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                '1',   '2',     '3',    '4',    '5',   '6',     '7',     '8',    '9']
    reversed_digits = [''.join(reversed(d)) for d in digits]

    conv = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
              '1': 1,   '2': 2,     '3': 3,    '4': 4,    '5': 5,   '6': 6,     '7': 7,     '8': 8,    '9': 9}
    conv.update({rd: conv[d] for d, rd in zip(digits, reversed_digits)})
    digits += reversed_digits

    cal_sum = 0
    for d in dat:
        idxs = {d.index(x): x for x in digits if x in d}
        c1 = min(idxs.items())

        reversed_d = ''.join(reversed(d))
        idxs = {reversed_d.index(x): x for x in digits if x in reversed_d}
        c2 = min(idxs.items())
        cal_sum += conv[c1[1]] * 10 + conv[c2[1]]

        if output:
            i1_s = c1[0]
            i1_e = c1[0] + len(c1[1])
            i2_e = len(d) - c2[0]
            i2_s = len(d) - c2[0] - len(c2[1])
            print(d[:i1_s] + ansi.blue(d[i1_s:i1_e]) + d[i1_e:i2_s] +
                            (ansi.blue(d[i2_s:i2_e]) if i1_s != i2_s else '') + d[i2_e:])

    return cal_sum

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
