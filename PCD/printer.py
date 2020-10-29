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
        print(f"\nDeactivate contact IN {contact.value} ({contact.name}).\n")

    def pulse(self, contact, time):
        print(f"\nActivate contact IN {contact.value}", end=' ')
        print(f"({contact.name})", end=' ')
        print(f"and turn it off after {time} second.\n")

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
        print(f"Is OUT {output.value} ({output.name}) inactive ?")

    def is_pulsing(self, output, frequency):
        print(f"Is OUT {output.value} ({output.name})", end=' ')
        print(f"pulsing with {frequency} Hz ?")

    def nothing_changes(self):
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every output unaltered ?")

    # get answers from user

    def wait_for_input(self):

        active = [int(x)
                  for x in
                  input("List answers for the questions: ").split(",")
                  ]
        print(active)


if __name__ == "__main__":
    from PCD.actions import action_1, action_11
    tb = TestBoxPrinter()
    action_1(tb)
    #  action_2(tb)
    action_11(tb)
    #  action_5(tb)

    # tb.wait_for_input()
