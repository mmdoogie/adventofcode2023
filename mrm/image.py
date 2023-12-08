from io import BytesIO
from subprocess import Popen, PIPE

from PIL import Image
from PIL.ImageDraw import Draw

def _min_pos(pos):
    min_x = min(p[0] for p in pos)
    min_y = min(p[1] for p in pos)

    return min_x, min_y

def _max_pos(pos):
    max_x = max(p[0] for p in pos)
    max_y = max(p[1] for p in pos)

    return max_x, max_y

def print_image(pos):
    min_x, min_y = _min_pos(pos)
    max_x, max_y = _max_pos(pos)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if [x, y] in pos:
                print('**', end = '')
            else:
                print('  ', end='')
        print()

def make_image(pos, output):
    min_x, min_y = _min_pos(pos)
    max_x, max_y = _max_pos(pos)

    width = max_x - min_x
    height = max_y - min_y

    img = Image.new('1', (2 * width + 2, height + 2), color = 1)
    draw = Draw(img)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if [x, y] in pos:
                draw.point(((x - min_x) * 2 + 1, y - min_y + 1), fill = 0)
                draw.point(((x - min_x) * 2 + 2, y - min_y + 1), fill = 0)
                if output:
                    print('**', end = '')
            elif output:
                print('  ', end='')
        if output:
            print()

    return img

def ocr_image(img):
    raw_io = BytesIO()
    img.save(raw_io, 'ppm')
    raw_io.seek(0)

    with Popen(["gocr", "-"], stdin=PIPE, stdout=PIPE) as gocr_proc:
        gocr_proc.stdin.write(raw_io.read())
        gocr_proc.stdin.close()
        gocr_proc.wait()
        txt = gocr_proc.stdout.read().decode('utf-8').strip('\n')
        gocr_proc.stdout.close()

    return txt
