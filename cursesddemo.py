#  I am a comment
import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_GREY = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)

    # stdscr.addstr(10, 10, "Hello Paul !",  BLUE_AND_YELLOW)
    # stdscr.addstr(12, 10, "Hello Caitlin !", GREEN_AND_GREY | curses.A_UNDERLINE | curses.A_BOLD)
    # stdscr.addstr(14, 10, "Hello Rory !", RED_AND_WHITE)

    for i in range(10):
        stdscr.clear()
        color = BLUE_AND_YELLOW
        if i % 2 == 0:
            color = GREEN_AND_GREY
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)

    stdscr.getch()


wrapper(main)
