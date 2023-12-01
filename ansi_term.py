from contextlib import contextmanager

ESC = chr(27)
CLEAR_LINE = ESC + '[K'

def clear_line():
    print(CLEAR_LINE)

def cursor_home():
    print(ESC + '[H')

def clear_screen():
    cursor_home()
    print(ESC + '[2J')

def red(txt):
    return ESC + '[31m' + txt + ESC + '[0m'

def green(txt):
    return ESC + '[32m' + txt + ESC + '[0m'

def yellow(txt):
    return ESC + '[33m' + txt + ESC + '[0m'

def blue(txt):
    return ESC + '[34m' + txt + ESC + '[0m'

def magenta(txt):
    return ESC + '[35m' + txt + ESC + '[0m'

def cyan(txt):
    return ESC + '[36m' + txt + ESC + '[0m'

def bold(txt):
    return ESC + '[1m' + txt + ESC + '[0m'

def italic(txt):
    return ESC + '[3m' + txt + ESC + '[0m'

def underline(txt):
    return ESC + '[4m' + txt + ESC + '[0m'

@contextmanager
def hidden_cursor():
    print(ESC + '[?25l')
    try:
        yield None
    finally:
        print(ESC + '[?25h')
