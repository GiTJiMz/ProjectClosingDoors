from PCD.printer import TestBoxPrinter

from PCD.actions import dict_actions

tb = TestBoxPrinter()

for k, v in dict_actions.items():
    print(k)
    if v(tb):
        continue
    else:
        break

# actions.action_1(tb)
# for action in dir(actions):
#     if action.startswith("action"):
#         getattr(actions, action)(tb)
#     print(action)

# print(dir(actions))
