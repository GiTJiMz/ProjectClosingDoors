from collections import namedtuple


class State(namedtuple("State", "inputs outputs pulsing")):

    def with_input(self, input):
        return self._replace(inputs=(self.inputs | {input}))

    def without_input(self, input):
        return self._replace(inputs=(self.inputs - {input}))

    def with_output(self, output):
        new_outputs = self.outputs | {output}
        return self._replace(outputs=new_outputs)

    def without_output(self, output):
        new_outputs = self.outputs - {output}
        return self._replace(outputs=new_outputs)

    def with_pulsing(self, output):
        new_pulsing = self.pulsing | {output}
        return self._replace(pulsing=new_pulsing)

    def without_pulsing(self, output):
        new_pulsing = self.pulsing - {output}
        return self._replace(pulsing=new_pulsing)


class StateMachineTextBox:

    def __init__(self):
        self.current_state = State(frozenset(), frozenset(), frozenset())
        self.future_actions = []

    def activate(self, contact):
        self.current_state = self.current_state.with_input(contact)

    def deactivate(self, contact):
        self.current_state = self.current_state.without_input(contact)

    def is_active(self, output, seconds=None):
        self.current_state = self.current_state.with_output(output).without_pulsing(output)
        if not seconds is None:
            self.future_actions.append((seconds, output))

    def is_inactive(self, output):
        self.current_state = self.current_state.without_output(output).without_pulsing(output)

    def pulse(self, contact, seconds=0):
        pass
        # self.current_state = self.current_state.with_input(contact)
        # self.future_actions.append((seconds, "DEACTIVATE", contact))

    def is_pulsing(self, output, freq):
        self.current_state = self.current_state.with_pulsing(output).without_output(output)

    def nothing_else_changes(self):
        pass

    def nothing_changes(self):
        pass

    def deactivate_all_other_input(self):
        pass


if __name__ == "__main__":
    import PCD.actions as actions

    box = StateMachineTextBox()

    actions.action_start_position(box)
    actions.action_1(box)

    states = {box.current_state: "init"}


    def state_name(state):
        if not state in states:
            states[state] = f"s{len(states):02d}"
        return states[state]

    print("digraph G {")

    for seq in actions.Sequence.instances.values():
        box = StateMachineTextBox()
        actions.action_start_position(box)
        actions.action_1(box)

        for action in seq.actions:
            before_s = state_name(box.current_state)
            action(box)
            after_s = state_name(box.current_state)
            print(f"{before_s} -> {after_s} [label = \" S{seq.id}:A{action.__name__[7:]}\"];")

            futures = box.future_actions
            box.future_actions = []
            for (secs, c) in sorted(futures):
                before_s = after_s
                box.is_inactive(c)
                after_s = state_name(box.current_state)
                print(f'{before_s} -> {after_s} [label = " S{seq.id}:{secs}s" style="dashed"];')

    print("}")

    for s, n in sorted(states.items(), key=lambda x: x[1]):
        print(n, ":")
        if s.inputs:
            print("  INPUTS:")
        for i in sorted(s.inputs):
            print("   ", i)
        if s.outputs:
            print("  OUTPUTS:")
        for o in sorted(s.outputs):
            print("   ", o)
        if s.pulsing:
            print("  PULSING:")
        for p in sorted(s.pulsing):
            print("   ", p)
