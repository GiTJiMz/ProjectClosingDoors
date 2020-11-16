# from PCD.printer import TestBoxPrinter
import curses
# import time

# from PCD.actions import dict_actions

# tb = TestBoxPrinter()


def menu(root, current_row):

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    height, width = root.getmaxyx()

    menu_options = ["Start automatic full test",
                    "Test specific function"]

    for index, element in enumerate(menu_options):
        y = height // 2 + index
        x = width // 2 - len(element) // 9

        if index == current_row:
            root.attron(curses.color_pair(1))
            root.addstr(y, x, element)
            root.attroff(curses.color_pair(1))

        else:
            root.addstr(y, x, element)

    root.refresh()
    # time.sleep(3)


def main(root):
    curses.curs_set(0)

    current_row = 0

    menu(root, current_row)

    while True:
        key = root.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        elif key == curses.KEY_DOWN and current_row < 1:
            current_row += 1

        elif key == ord("e"):
            break

        elif key == ord("q"):
            break

        menu(root, current_row)

    root.refresh()


curses.wrapper(main)

# menu():

# Start full test

# Test specific door function

#       Door function 1 (run actions 2-12)
#       Door function 2 (run actions 3-20)
#       Door function 3 (run actions 21-37)

#       Door function 4 (run actions 38-48)
#       Door function 5 (run actions 49-56)
#       Door function 6 (run actions 57-73)

#       Door function 7 (run actions 74-91)
#       Door function 8 (run actions 92-101)
#       Door function 9 (run actions 102-111)
#       Door function 10 (run actions 112-113)


# for k, v in dict_actions.items():
#     print(k)
#     v(tb)
#     answer = tb.wait_for_input()
#     if tb.treat_input(answer):
#         continue
#     else:
#         break

# actions.action_1(tb)
# for action in dir(actions):
#     if action.startswith("action"):
#         getattr(actions, action)(tb)
#     print(action)

# print(dir(actions))
