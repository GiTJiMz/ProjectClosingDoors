class TestBoxPrinter:

    activation = False  # Indicates wheather activation has occurred

    # ask user to do actions on input

    def activate(self, contact):
        if self.activation is False:
            if contact.value == 0:
                print(f"\nActivate {contact.name} contact.")
            else:
                print(f"\nActivate contact IN", end=' ')
                print(f"{contact.value} ({contact.name}).")
            self.activation = True
        else:
            if contact.value == 0:
                print(f"Activate {contact.name} contact.")
            else:
                print(f"Activate contact IN {contact.value} ({contact.name}).")

    def deactivate(self, contact):
        if self.activation is False:
            if contact.value == 0:
                print(f"\nDeactivate {contact.name} contact.")
            else:
                print(f"\nDeactivate contact IN", end=' ')
                print(f"{contact.value} ({contact.name}).")
            self.activation = True
        else:
            if contact.value == 0:
                print(f"Deactivate {contact.name} contact.")
            else:
                print(f"Deactivate contact IN", end=' ')
                print(f"{contact.value} ({contact.name}).")

    def deactivate_all_other_input(self):
        print(f"\nDeactivate all other input")

    def pulse(self, contact, time=0):
        print(f"\nActivate contact IN {contact.value}", end=' ')
        print(f"({contact.name})", end=' ')
        print(f"and turn it off after {time} seconds.\n")

    # ask user to check on output

    def is_active(self, output, time=None):
        if self.activation is True:
            print("")
            self.activation = False

        if time is None:
            print(f"Is OUT {output.value} ({output.name}) active ?")
        else:
            print(f"Is OUT {output.value} ({output.name})", end=' ')
            print(f"active for {time} seconds ?")

    def is_inactive(self, output):
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is OUT {output.value} ({output.name}) inactive ?")

    def is_pulsing(self, output, frequency):
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is OUT {output.value} ({output.name})", end=' ')
        print(f"pulsing with {frequency} Hz ?")

    def nothing_changes(self):
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every output unaltered ?")

    def nothing_else_changes(self):
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every other output unaltered ?")

    def everything_else_deactivated(self):
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every other output deactivated ?")

    # get answers from user

    def wait_for_input(self):
        active = [int(x)
                  for x in
                  input("List answers for the questions: ").split(",")
                  ]
        print(active)
        return active

    def treat_input(self, answer):
        print("Treating input from user")
        return True


# class AdvancedTestBoxPrinter:
#
#     def __init__(self):
#         self.active = []
#
#     def is_active(self, output, time=None):
#         self.active.append(output)
#
#     def wait_for_input(self):
#         for active in self.active:
#             print(f"Is output {active} active")
#
#     def treat_input(self, answer):
#         pass
#         # lookup answer in active
#         # for a in answer:
#         #     self.active[a.index]


if __name__ == "__main__":
    from PCD import actions
    tb = TestBoxPrinter()
    actions.action_1(tb)
    actions.action_2(tb)
    actions.action_11(tb)
    actions.action_5(tb)
    actions.action_29(tb)
    actions.action_33(tb)

    # tb.wait_for_input()
