#  I am a comment
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)



    """ 
      key = stdscr.getkey()
    stdscr.addstr(10, 10, f"Key: {key}")
    stdscr.refresh()
    stdscr.getch()
    """
    """ 
    x, y, = 0, 0
    string_x = 0
    stdscr.nodelay(True)

    while True:

        try:
            key = stdscr.getkey()
        except:
            key = None
        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
        stdscr.clear()
        string_x += 1
        stdscr.addstr(0, string_x // 500, "Hello Paul !")
        stdscr.addstr(y, x, "0")
        stdscr.refresh()
        """

    curses.echo()

    stdscr.attron(RED_AND_WHITE)
    stdscr.border()
    stdscr.attroff(RED_AND_WHITE)

    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.attroff(GREEN_AND_BLACK)

    stdscr.addstr(3, 3, "Hello Paul!")
    stdscr.move(10, 50)

    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        if key == "q":
            break

    stdscr.getch()


wrapper(main)
