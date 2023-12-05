import sys
import ansi_term as ansi
from time import sleep

with open('data/aoc-2023-04.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

leftcol = 1
currrow = 1
def tprint(x='', **kwargs):
    global currrow
    if 'end' in kwargs:
        print(x, **kwargs)
    else:
        print(ansi.ESC + f'[{currrow};{leftcol}H' + x, **kwargs, end='')
        currrow += 1
        print(ansi.ESC + f'[{currrow};{leftcol}H', **kwargs, end='')

def part1(output = True):
    global currrow, leftcol
    total_points = 0
    ansi.clear_screen()

    with ansi.hidden_cursor():

        resetrow = 1
        for d in dat:
            win_numbers, my_numbers = d.split(': ')[1].split(' | ')
            win_numbers = [int(x) for x in win_numbers.split(' ') if x != '']
            my_numbers = [int(x) for x in my_numbers.split(' ') if x != '']

            card_matches = sum(w in my_numbers for w in win_numbers)
            if card_matches >= 1:
                total_points += pow(2, card_matches - 1)

            #ansi.clear_screen()
            currrow = resetrow
            gid = d.split(':')[0]
            tprint('  ' + ansi.underline(ansi.cyan('Scratch-off ' + gid)))
            tprint()
            tprint('      ' + ansi.underline(ansi.yellow('Your Numbers')))
            for i in range(5):
                tprint('     ', end = '')
                for v in my_numbers[5*i:5*i+5]:
                    if v in win_numbers:
                        tprint(ansi.magenta(f'{v:2d} '), end='')
                    else:
                        tprint(f'{v:2d} ', end='')
                tprint()
            tprint()
            tprint('     ' + ansi.underline(ansi.magenta('Winning Numbers')))
            for i in range(2):
                tprint('     ', end = '')
                for v in win_numbers[5*i:5*i+5]:
                    if v in my_numbers:
                        tprint(ansi.yellow(f'{v:2d} '), end='')
                    else:
                        tprint(f'{v:2d} ', end='')
                tprint()
            tprint()

            if card_matches == 0:
                tprint(ansi.red(' Sorry, not a winner :('))
            else:
                tprint(ansi.green(' Congrats! You win ' + str(pow(2, card_matches - 1))))
            tprint(ansi.green(' Total winnings: ' + str(total_points)))
            tprint()
            sys.stdout.flush()
            sleep(0.05)
            leftcol += 25
            if leftcol >= 7*25:
                leftcol = 0
                resetrow += 18
                if resetrow >= 3*18:
                    resetrow = 1
                    sleep(0.5)
                    ansi.clear_screen()

    print()

    return total_points

def print_counts(card_counts, card_points, highlight):
    ansi.cursor_home()
    for y in range(50):
        for i in range(len(card_counts)//50 + 1):
            cn = y + 50*i
            if cn == highlight:
                print(ansi.COLOR_BLUE, end='')
            elif cn > highlight and cn <= highlight + card_points[highlight]:
                print(ansi.COLOR_YELLOW, end='')
            else:
                print(ansi.TEXT_RESET, end='')
            if cn in card_counts:
                if card_points[cn] > 0:
                    winstr = 'W' + f'{card_points[cn]:2d}'
                else:
                    winstr = 'L  '
                print(f'Card {cn + 1:3d}: {winstr} Have: {card_counts[cn]:7d},     ', end='')
        print()
    print()
    print(f'Total Count: {sum(card_counts.values())}')

def part2(output = True):
    sleep(1)
    ansi.clear_screen() 
    st = 0.5

    with ansi.hidden_cursor():
        card_points = {}
        card_counts = {}

        for i, d in enumerate(dat):
            win_numbers, my_numbers = d.split(': ')[1].split(' | ')
            win_numbers = [int(x) for x in win_numbers.split(' ') if x != '']
            my_numbers = [int(x) for x in my_numbers.split(' ') if x != '']

            card_points[i] = sum(w in my_numbers for w in win_numbers)
            card_counts[i] = 1

        for i, pts in card_points.items():
            print_counts(card_counts, card_points, i)
            sys.stdout.flush()
            for x in range(pts):
                card_counts[i + 1 + x] += card_counts[i]
            sleep(st)
            print_counts(card_counts, card_points, i)
            sys.stdout.flush()
            sleep(st)

            if i == 10:
                st = 0.05

    return sum(card_counts.values())

if __name__ == '__main__':
    tprint('Part 1:', part1(True))
    tprint('Part 2:', part2(True))
