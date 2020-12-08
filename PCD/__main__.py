import cmd

import PCD.actions as actions
from PCD.actions import Sequence
from PCD.printer import TestBoxPrinter


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

    def _run_action(self, action, seq=None):
        if seq is None:
            if action.__name__ == "action_power_off":
                action(self.tb)
            elif action.__name__ == "action_start_position":
                print(f"\nPut testbox in startposition by executing {action.__name__}:\n")
                action(self.tb)
        else:
            print("\nTesting:", action.__name__)
            action(self.tb)
            answer = self.tb.wait_for_input()
            if not answer:
                print(f"\nError message for {action.__name__} in door-function {seq.id}:\n"
                      f"{action.__doc__}")
            return answer

    def _run_sequence(self, seq):
        print("\nTesting:", seq)
        self._run_action(actions.action_power_off)
        self._run_action(actions.action_start_position)
        answer = self._run_action(actions.action_1, seq)
        if not answer:
            return False
        for action in seq.actions:
            if not self._run_action(action, seq):
                return False
        return True

    def do_test(self, args):
        """Run a full test or a test of a specific door-function.

        The starting point for all tests is as follows.

        1. Turn off test box
        2. Disable all contacts

        So make sure to carry out the above steps before initiating any tests.

        Testing is done writing the commands below.

        pcd> test all - runs a full test (all door-functions are tested one by one)
        pcd> test 1 - example that runs a test of door-function 1
        """
        if args == "all":
            for k, v in sorted(Sequence.instances.items()):
                if not self._run_sequence(v):
                    return
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
