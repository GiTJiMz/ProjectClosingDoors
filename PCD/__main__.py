from PCD.printer import TestBoxPrinter

from PCD import actions

tb = TestBoxPrinter()

# actions.action_1(tb)
for action in dir(actions):
    if action.startswith("action"):
        getattr(actions, action)(tb)
    print(action)

# print(dir(actions))
