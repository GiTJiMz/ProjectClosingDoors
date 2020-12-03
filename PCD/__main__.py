import cmd

from PCD.actions import Sequence
from PCD.printer import TestBoxPrinter
from PCD.error_messages import error_messages


class PCDHandler(cmd.Cmd):

    intro = """
 Welcome to Project Closing Doors.
 The purpose of this program is to test
 the Door Control Unit, installed in IC3 trains
 """

    prompt = "pcd> "

    def __init__(self, tb: TestBoxPrinter):
        super().__init__()
        self.tb = tb

    def _run_sequence(self, seq):
        print("\nTesting:", seq)
        for action in seq.actions:
            print("\nTesting:", action.__name__)
            action(self.tb)
            answer = self.tb.wait_for_input()
            if answer == "n":
                pass

                print(f"\nError message for {action.__name__} in door-function {seq.id}:\n"
                      f"{error_messages[action.__name__]}")
                break
            # if not self.tb.treat_input(answer):
            #     print("Not a valid input")
            #     break

    def do_test(self, args):
        """Run a full test or a test of a specific door-function.

        The starting point for all tests is as follows.

        1. Turn off test box
        2. Disable all contacts

        So make sure to carry out the above steps before initiating any tests.

        Testing is done writing the

        pcd> test all - runs a full test (all door-functions are tested one by one)
        pcd> test 1 - example that runs a test of door-function 1
        """
        if args == "all":
            for k, v in sorted(Sequence.instances.items()):
                self._run_sequence(v)
            return

        try:
            seqid = int(args)
        except ValueError as e:
            print(f"Invalid syntax")
        else:
            seq = Sequence.instances[seqid]
            self._run_sequence(seq)

    def do_list(self, args):
        """ Lists all door-functions """
        for id, seq in Sequence.instances.items():
            print("-", seq, "\n")

    def do_EOF(self, line):
        """ Ends the program """
        return True


if __name__ == "__main__":
    PCDHandler(TestBoxPrinter()).cmdloop()