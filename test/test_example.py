from PCD.statemachine import StateMachineTestBox, State
from PCD.domain import Input, Output


def test_istrue():
    assert True


def test_state_machine_should_add_input_when_activated():
    box = StateMachineTestBox()
    box.activate(Input.FREEGIVING_OF_DOOR_L)

    assert box.current_state == State.empty().with_input(Input.FREEGIVING_OF_DOOR_L)


def test_state_machine_should_add_output_when_is_active():
    box = StateMachineTestBox()
    box.is_active(Output.ATTENTION_SIGNAL_DOOR_LEFT)

    # TODO: This fails! fix the test, what should this be?
    assert box.current_state == State.empty()
