#  I am a comment
import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10, "Hello Paul !", curses.A_UNDERLINE  )
    stdscr.addstr(15, 25, "Hello Caitlin !")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
