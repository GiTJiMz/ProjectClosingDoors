class TestBoxPrinter:

    def __init__(self):
        self.questions = 0
        # Indicates wheather activation has occurred
        self.activation = False

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
        self.questions += 1
        if self.activation is True:
            print("")
            self.activation = False

        if time is None:
            print(f"Is OUT {output.value} ({output.name}) active ?")
        else:
            print(f"Is OUT {output.value} ({output.name})", end=' ')
            print(f"active for {time} seconds ?")

    def is_inactive(self, output):
        self.questions += 1
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is OUT {output.value} ({output.name}) inactive ?")

    def is_pulsing(self, output, frequency):
        self.questions += 1
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is OUT {output.value} ({output.name})", end=' ')
        print(f"pulsing with {frequency} Hz ?")

    def nothing_changes(self):
        self.questions += 1
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every output unaltered ?")

    def nothing_else_changes(self):
        self.questions += 1
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every other output unaltered ?")

    def everything_else_deactivated(self):
        self.questions += 1
        if self.activation is True:
            print("")
            self.activation = False

        print(f"Is every other output deactivated ?")

    # get answers from user

    def wait_for_input(self):
        answer = None
        while True:
            if answer is not None:
                answer = input("Answer the question by typing y or n and hit enter: ").lower()
            else:
                answer = input("\nCan you confirm correctness of all of the above questions ? [y/n]: ").lower()
            if answer in ['y', 'n']:
                return answer

    # def treat_input(self, answer):
    #     noquestion, self.questions = self.questions, 0
    #     return len(answer) == noquestion and all(answer)
