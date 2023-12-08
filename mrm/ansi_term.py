from contextlib import contextmanager

ESC = chr(27)

CURSOR_HOME = ESC + '[H'
CLEAR_SCREEN = CURSOR_HOME + ESC + '[2J'
CLEAR_LINE = ESC + '[K'

COLOR_RED = ESC + '[31m'
COLOR_GREEN = ESC + '[32m'
COLOR_YELLOW = ESC + '[33m'
COLOR_BLUE = ESC + '[34m'
COLOR_MAGENTA = ESC + '[35m'
COLOR_CYAN = ESC + '[36m'

TEXT_BOLD = ESC + '[1m'
TEXT_ITALIC = ESC + '[3m'
TEXT_UNDERLINE = ESC + '[4m'
TEXT_RESET = ESC + '[0m'

SAVE_CURSOR = ESC + '[s'
RESTORE_CURSOR = ESC + '[u'

HIDE_CURSOR = ESC + '[?25l'
SHOW_CURSOR = ESC + '[?25h'

def clear_line():
    print(CLEAR_LINE, end = '')

def cursor_home():
    print(CURSOR_HOME, end = '')

def clear_screen():
    print(CLEAR_SCREEN, end = '')

def red(txt):
    return COLOR_RED + txt + TEXT_RESET

def green(txt):
    return COLOR_GREEN + txt + TEXT_RESET

def yellow(txt):
    return COLOR_YELLOW + txt + TEXT_RESET

def blue(txt):
    return COLOR_BLUE + txt + TEXT_RESET

def magenta(txt):
    return COLOR_MAGENTA + txt + TEXT_RESET

def cyan(txt):
    return COLOR_CYAN + txt + TEXT_RESET

def bold(txt):
    return TEXT_BOLD + txt + TEXT_RESET

def italic(txt):
    return TEXT_ITALIC + txt + TEXT_RESET

def underline(txt):
    return TEXT_UNDERLINE + txt + TEXT_RESET

def save_cursor():
    print(SAVE_CURSOR, end = '')

def restore_cursor():
    print(RESTORE_CURSOR, end = '')

@contextmanager
def restored_cursor():
    restore_cursor()
    try:
        yield None
    finally:
        save_cursor()

@contextmanager
def hidden_cursor():
    print(HIDE_CURSOR, end = '')
    try:
        yield None
    finally:
        print(SHOW_CURSOR, end = '')
