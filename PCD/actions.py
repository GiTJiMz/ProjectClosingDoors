from PCD.domain import Input, Output


class Sequence:
    instances = {}

    def __init__(self, id: int, description="", actions=None):
        self.id = id
        self.description = description
        self.actions = actions or []
        Sequence.instances[id] = self

    def declare_action(self, action):
        self.actions.append(action)
        return action

    def __str__(self):
        return f"Door-function {self.id}: {self.description} " \
               + f"[{len(self.actions)}]"


# Power-off

def action_power_off(tb):
    tb.deactivate(Input(0))


# Start position

def action_start_position(tb):
    tb.activate(Input(8))
    tb.activate(Input(9))
    tb.activate(Input(10))
    tb.activate(Input(11))
    tb.deactivate_all_other_input()


# Power-on test

def action_1(tb):
    """\nThis is a placeholder text for error message in action_1\n"""
    tb.activate(Input(0))  # Input(0) = Input.POWER
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    tb.nothing_else_changes()


# Test of right door side

seq1 = Sequence(1, "Test of local operation of right door")


@seq1.declare_action
def action_2(tb):
    """\nIf one or more errors occur when this action is carried out, hints for troubleshooting are given below for
each individual input and output:

Hints for,


Error on IN 2 (FREEGIVING_OF_DOOR_R):

  -  Troubleshooting is done on the CPU PCB

  -  Before troubleshooting any of the outputs, start by verifying activation of IN 2, by measuring 24V
     on the resistor R36. Follow the signal and verify that you can measure it on IC N3: pin 7 and pin 1.
     If you can't verify the signal, replace IC N3.
     If the signal is ok, the last place to verify the activation of IN 2 is by measuring the signal on IC D7: pin 8.
     If you can't verify the signal at this point, replace IC D7
     Run/rerun test of door-function 1 and verify whether IN 2 is working as is should or not,
     when this action is carried out.
     If the signal is ok, you can go on and troubleshoot the output signals.


Error on OUT 3 (ACKNOWLEDGE_FOR_FREEGIVING_OF_DOORS):

  -  Troubleshooting is done on the CPU PCB

  -  Verify the active signal by measuring 24V on IC D2: pin 14. If it's not active, replace IC D2.
     If you can verify the active signal on IC D2: pin 14, power off the testbox and measure output transistor V7 and
     diode V15 to check for short circuits and disconnections. If V7 and / or V15 are defective, replace the
     respective components. Run/rerun test of door-function 1 and verify whether OUT 3 is working as is should or not,
     when this action is carried out.


Error on OUT 12 (OPENING_LIGHT_FOR_PUSHBUTTON_R):

  -  Troubleshooting is done on the CPU PCB

  -  Verify the active signal by measuring 24V on IC D3: pin 13. If it's not active, replace IC D3.
     If you can verify the active signal on IC D3: pin 13, power off the testbox and measure output transistor V20 and
     diode V37 to check for short circuits and disconnections. If V20 and / or V37 are defective, replace the
     respective components. Run/rerun test of door-function 1 and verify whether OUT 12 is working as is should or not,
     when this action is carried out.


Error on OUT 4 (ATTENTION_SIGNAL_DOOR_RIGHT):

  -  Troubleshooting is done on the CPU PCB

  -  Verify the pulsing signal by measuring a change in signal from 0V to 24V and back to 0V 4 seconds later
     on IC D2: pin 13. To catch this measurement, you need set up the measurement first and rerun the test of
     door-function 1. If it's not pulsing, replace IC D2. If you can verify the pulsing signal on D2: pin 13,
     power off the testbox and measure output transistor V4 and diode V12 to check for short circuits and
     disconnections. If V4 and / or V12 are defective, replace the respective components.
     Run/rerun test of door-function 1 and verify whether OUT 4 is working as is should or not,
     when this action is carried out.


If nothing of the above is working, try burning a new EPROM with new software.
"""
    tb.activate(Input(2))  # Input(2) = Input.IN_2
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()


@seq1.declare_action
def action_3(tb):
    """\nThis is a placeholder text for error message in action_3\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq1.declare_action
def action_4(tb):
    """\nThis is a placeholder text for error message in action_4\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq1.declare_action
def action_5(tb):
    """\nThis is a placeholder text for error message in action_5\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq1.declare_action
def action_6(tb):
    """\nThis is a placeholder text for error message in action_6\n"""
    tb.pulse(Input(6))
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq1.declare_action
def action_7(tb):
    """\nThis is a placeholder text for error message in action_7\n"""
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.nothing_changes()


@seq1.declare_action
def action_8(tb):
    """\nThis is a placeholder text for error message in action_8\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq1.declare_action
def action_9(tb):
    """\nThis is a placeholder text for error message in action_9\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.nothing_changes()


@seq1.declare_action
def action_10(tb):
    """\nThis is a placeholder text for error message in action_10\n"""
    tb.pulse(Input(6))
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq1.declare_action
def action_11(tb):
    """\nThis is a placeholder text for error message in action_11\n"""
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.nothing_changes()


@seq1.declare_action
def action_12(tb):
    """\nThis is a placeholder text for error message in action_12\n"""
    tb.deactivate(Input(2))
    tb.is_active(Output(1))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(13))
    tb.nothing_else_changes()


seq2 = Sequence(2, """Test of attention signal to TGF,
                   when right door is local operated
                   and acknowledge for freegiving of doors
                   is deactivated.
                   The door closed signal for right door is also tested""")


@seq2.declare_action
def action_13(tb):
    """\nThis is a placeholder text for error message in action_13\n"""
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()


@seq2.declare_action
def action_14(tb):
    """\nThis is a placeholder text for error message in action_14\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq2.declare_action
def action_15(tb):
    """\nThis is a placeholder text for error message in action_15\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq2.declare_action
def action_16(tb):
    """\nThis is a placeholder text for error message in action_16\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq2.declare_action
def action_17(tb):
    """\nThis is a placeholder text for error message in action_17\n"""
    tb.deactivate(Input(2))
    tb.is_pulsing(Output(13), 3)
    tb.nothing_else_changes()


@seq2.declare_action
def action_18(tb):
    """\nThis is a placeholder text for error message in action_18\n"""
    tb.pulse(Input(6))
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq2.declare_action
def action_19(tb):
    """\nThis is a placeholder text for error message in action_19\n"""
    tb.activate(Input(8))
    tb.is_pulsing(Output(1), 1)
    tb.nothing_else_changes()


@seq2.declare_action
def action_20(tb):
    """\nThis is a placeholder text for error message in action_20\n"""
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()


seq3 = Sequence(3, "Test of service-access in left doorside (e.g. to fill up catering)")


@seq3.declare_action
def action_21(tb):
    """\nThis is a placeholder text for error message in action_21\n"""
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()


@seq3.declare_action
def action_22(tb):
    """\nThis is a placeholder text for error message in action_22\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq3.declare_action
def action_23(tb):
    """\nThis is a placeholder text for error message in action_23\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq3.declare_action
def action_24(tb):
    """\nThis is a placeholder text for error message in action_24\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq3.declare_action
def action_25(tb):
    """\nThis is a placeholder text for error message in action_25\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(9))
    tb.nothing_else_changes()


@seq3.declare_action
def action_26(tb):
    """\nThis is a placeholder text for error message in action_26\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq3.declare_action
def action_27(tb):
    """\nThis is a placeholder text for error message in action_27\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq3.declare_action
def action_28(tb):
    """\nThis is a placeholder text for error message in action_28\n"""
    tb.pulse(Input(14))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()


@seq3.declare_action
def action_29(tb):
    """\nThis is a placeholder text for error message in action_29\n"""
    tb.activate(Input(9))
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()


@seq3.declare_action
def action_30(tb):
    """\nThis is a placeholder text for error message in action_30\n"""
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()


@seq3.declare_action
def action_31(tb):
    """\nThis is a placeholder text for error message in action_31\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(9))
    tb.nothing_else_changes()


@seq3.declare_action
def action_32(tb):
    """\nThis is a placeholder text for error message in action_32\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq3.declare_action
def action_33(tb):
    """\nThis is a placeholder text for error message in action_33\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq3.declare_action
def action_34(tb):
    """\nThis is a placeholder text for error message in action_34\n"""
    tb.deactivate(Input(2))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.is_pulsing(Output(13), 3)
    tb.nothing_else_changes()


@seq3.declare_action
def action_35(tb):
    """\nThis is a placeholder text for error message in action_35\n"""
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()


@seq3.declare_action
def action_36(tb):
    """\nThis is a placeholder text for error message in action_36\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq3.declare_action
def action_37(tb):
    """\nThis is a placeholder text for error message in action_37\n"""
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()


# Test of left door side

seq4 = Sequence(4, "Test of local operation of left door")


@seq4.declare_action
def action_38(tb):
    """\nThis is a placeholder text for error message in action_38\n"""
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()


@seq4.declare_action
def action_39(tb):
    """\nThis is a placeholder text for error message in action_39\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq4.declare_action
def action_40(tb):
    """\nThis is a placeholder text for error message in action_40\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq4.declare_action
def action_41(tb):
    """\nThis is a placeholder text for error message in action_41\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq4.declare_action
def action_42(tb):
    """\nThis is a placeholder text for error message in action_42\n"""
    tb.pulse(Input(14))
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()


@seq4.declare_action
def action_43(tb):
    """\nThis is a placeholder text for error message in action_43\n"""
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.nothing_changes()


@seq4.declare_action
def action_44(tb):
    """\nThis is a placeholder text for error message in action_44\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq4.declare_action
def action_45(tb):
    """\nThis is a placeholder text for error message in action_45\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.nothing_changes()


@seq4.declare_action
def action_46(tb):
    """\nThis is a placeholder text for error message in action_46\n"""
    tb.pulse(Input(14))
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()


@seq4.declare_action
def action_47(tb):
    """\nThis is a placeholder text for error message in action_47\n"""
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.nothing_changes()


@seq4.declare_action
def action_48(tb):
    """\nThis is a placeholder text for error message in action_48\n"""
    tb.deactivate(Input(3))
    tb.is_active(Output(2))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(11))
    tb.nothing_else_changes()


seq5 = Sequence(5, """Test of attention signal to TGF,
                   when left door is local operated
                   and acknowledge for freegiving of doors
                   is deactivated.
                   The door closed signal for left door is also tested""")


@seq5.declare_action
def action_49(tb):
    """\nThis is a placeholder text for error message in action_49\n"""
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()


@seq5.declare_action
def action_50(tb):
    """\nThis is a placeholder text for error message in action_50\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq5.declare_action
def action_51(tb):
    """\nThis is a placeholder text for error message in action_51\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq5.declare_action
def action_52(tb):
    """\nThis is a placeholder text for error message in action_52\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq5.declare_action
def action_53(tb):
    """\nThis is a placeholder text for error message in action_53\n"""
    tb.deactivate(Input(3))
    tb.is_pulsing(Output(11), 3)
    tb.nothing_else_changes()


@seq5.declare_action
def action_54(tb):
    """\nThis is a placeholder text for error message in action_54\n"""
    tb.pulse(Input(14))
    tb.is_active(Output(19))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()


@seq5.declare_action
def action_55(tb):
    """\nThis is a placeholder text for error message in action_55\n"""
    tb.activate(Input(9))
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()


@seq5.declare_action
def action_56(tb):
    """\nThis is a placeholder text for error message in action_56\n"""
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()


seq6 = Sequence(6, "Test of service-access in left doorside (e.g. to fill up catering)")


@seq6.declare_action
def action_57(tb):
    """\nThis is a placeholder text for error message in action_57\n"""
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()


@seq6.declare_action
def action_58(tb):
    """\nThis is a placeholder text for error message in action_58\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq6.declare_action
def action_59(tb):
    """\nThis is a placeholder text for error message in action_59\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq6.declare_action
def action_60(tb):
    """\nThis is a placeholder text for error message in action_60\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq6.declare_action
def action_61(tb):
    """\nThis is a placeholder text for error message in action_61\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(12))
    tb.nothing_else_changes()


@seq6.declare_action
def action_62(tb):
    """\nThis is a placeholder text for error message in action_62\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq6.declare_action
def action_63(tb):
    """\nThis is a placeholder text for error message in action_63\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq6.declare_action
def action_64(tb):
    """\nThis is a placeholder text for error message in action_64\n"""
    tb.pulse(Input(6))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq6.declare_action
def action_65(tb):
    """\nThis is a placeholder text for error message in action_65\n"""
    tb.activate(Input(8))
    tb.is_pulsing(Output(1), 1)
    tb.nothing_else_changes()


@seq6.declare_action
def action_66(tb):
    """\nThis is a placeholder text for error message in action_66\n"""
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()


@seq6.declare_action
def action_67(tb):
    """\nThis is a placeholder text for error message in action_67\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(12))
    tb.nothing_else_changes()


@seq6.declare_action
def action_68(tb):
    """\nThis is a placeholder text for error message in action_68\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq6.declare_action
def action_69(tb):
    """\nThis is a placeholder text for error message in action_69\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq6.declare_action
def action_70(tb):
    """\nThis is a placeholder text for error message in action_70\n"""
    tb.deactivate(Input(3))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.is_pulsing(Output(11), 3)
    tb.nothing_else_changes()


@seq6.declare_action
def action_71(tb):
    """\nThis is a placeholder text for error message in action_71\n"""
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()


@seq6.declare_action
def action_72(tb):
    """\nThis is a placeholder text for error message in action_72\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(19))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()


@seq6.declare_action
def action_73(tb):
    """\nThis is a placeholder text for error message in action_73\n"""
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()


seq7 = Sequence(7, "Test of blocking of doors and manual operation")


@seq7.declare_action
def action_74(tb):
    """\nThis is a placeholder text for error message in action_74\n"""
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()


@seq7.declare_action
def action_75(tb):
    """\nThis is a placeholder text for error message in action_75\n"""
    tb.activate(Input(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()


@seq7.declare_action
def action_76(tb):
    """\nThis is a placeholder text for error message in action_76\n"""
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq7.declare_action
def action_77(tb):
    """\nThis is a placeholder text for error message in action_77\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq7.declare_action
def action_78(tb):
    """\nThis is a placeholder text for error message in action_78\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq7.declare_action
def action_79(tb):
    """\nThis is a placeholder text for error message in action_79\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq7.declare_action
def action_80(tb):
    """\nThis is a placeholder text for error message in action_80\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq7.declare_action
def action_81(tb):
    """\nThis is a placeholder text for error message in action_81\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.nothing_else_changes()


@seq7.declare_action
def action_82(tb):
    """\nThis is a placeholder text for error message in action_82\n"""
    tb.deactivate(Input(2))
    tb.deactivate(Input(3))
    tb.is_pulsing(Output(11), 3)
    tb.is_pulsing(Output(13), 3)
    tb.nothing_else_changes()


@seq7.declare_action
def action_83(tb):
    """\nThis is a placeholder text for error message in action_83\n"""
    tb.activate(Input(4))
    tb.is_active(Output(172))
    tb.is_active(Output(171))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(15))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq7.declare_action
def action_84(tb):
    """\nThis is a placeholder text for error message in action_84\n"""
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()


@seq7.declare_action
def action_85(tb):
    """\nThis is a placeholder text for error message in action_85\n"""
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()


@seq7.declare_action
def action_86(tb):
    """\nThis is a placeholder text for error message in action_86\n"""
    tb.activate(Input(16))
    tb.is_inactive(Output(172))
    tb.is_inactive(Output(171))
    tb.is_inactive(Output(19))
    tb.is_inactive(Output(20))
    tb.is_pulsing(Output(1), 1)
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()


@seq7.declare_action
def action_87(tb):
    """\nThis is a placeholder text for error message in action_87\n"""
    tb.deactivate(Input(8))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq7.declare_action
def action_88(tb):
    """\nThis is a placeholder text for error message in action_88\n"""
    tb.deactivate(Input(9))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq7.declare_action
def action_89(tb):
    """\nThis is a placeholder text for error message in action_89\n"""
    tb.activate(Input(8))
    tb.activate(Input(9))
    tb.is_pulsing(Output(1), 1)
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()


@seq7.declare_action
def action_90(tb):
    """\nThis is a placeholder text for error message in action_90\n"""
    tb.deactivate(Input(16))
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(172))
    tb.is_active(Output(171))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    tb.nothing_else_changes()


@seq7.declare_action
def action_91(tb):
    """\nThis is a placeholder text for error message in action_91\n"""
    tb.deactivate(Input(4))
    tb.is_inactive(Output(172))
    tb.is_inactive(Output(171))
    tb.nothing_else_changes()


seq8 = Sequence(8, "Test of central closing of doors, when right door is local operated")


@seq8.declare_action
def action_92(tb):
    """\nThis is a placeholder text for error message in action_92\n"""
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()


@seq8.declare_action
def action_93(tb):
    """\nThis is a placeholder text for error message in action_93\n"""
    tb.activate(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()


@seq8.declare_action
def action_94(tb):
    """\nThis is a placeholder text for error message in action_94\n"""
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()


@seq8.declare_action
def action_95(tb):
    """\nThis is a placeholder text for error message in action_95\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq8.declare_action
def action_96(tb):
    """\nThis is a placeholder text for error message in action_96\n"""
    tb.activate(Input(1))
    tb.is_pulsing(Output(7), 5)
    tb.is_pulsing(Output(8), 5)
    tb.is_pulsing(Output(182), 5)
    tb.is_pulsing(Output(181), 5)
    tb.nothing_else_changes()


@seq8.declare_action
def action_97(tb):
    """\nThis is a placeholder text for error message in action_97\n"""
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(3))
    tb.is_inactive(Output(13))
    tb.is_pulsing(Output(14), 5)
    tb.nothing_else_changes()


@seq8.declare_action
def action_98(tb):
    """\nThis is a placeholder text for error message in action_98\n"""
    tb.pulse(Input(6))
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()


@seq8.declare_action
def action_99(tb):
    """\nThis is a placeholder text for error message in action_99\n"""
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()


@seq8.declare_action
def action_100(tb):
    """\nThis is a placeholder text for error message in action_100\n"""
    tb.deactivate(Input(1))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    tb.nothing_else_changes()


@seq8.declare_action
def action_101(tb):
    """\nThis is a placeholder text for error message in action_101\n"""
    tb.deactivate(Input(2))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(12))
    tb.nothing_else_changes()


seq9 = Sequence(9, "Test of central closing of doors, when left door is local operated")


@seq9.declare_action
def action_102(tb):
    """\nThis is a placeholder text for error message in action_102\n"""
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()


@seq9.declare_action
def action_103(tb):
    """\nThis is a placeholder text for error message in action_103\n"""
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()


@seq9.declare_action
def action_104(tb):
    """\nThis is a placeholder text for error message in action_104\n"""
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()


@seq9.declare_action
def action_105(tb):
    """\nThis is a placeholder text for error message in action_105\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()


@seq9.declare_action
def action_106(tb):
    """\nThis is a placeholder text for error message in action_106\n"""
    tb.activate(Input(1))
    tb.is_pulsing(Output(7), 5)
    tb.is_pulsing(Output(8), 5)
    tb.is_pulsing(Output(182), 5)
    tb.is_pulsing(Output(181), 5)
    tb.nothing_else_changes()


@seq9.declare_action
def action_107(tb):
    """\nThis is a placeholder text for error message in action_107\n"""
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(3))
    tb.is_inactive(Output(11))
    tb.is_pulsing(Output(10), 5)
    tb.nothing_else_changes()


@seq9.declare_action
def action_108(tb):
    """\nThis is a placeholder text for error message in action_108\n"""
    tb.pulse(Input(14))
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()


@seq9.declare_action
def action_109(tb):
    """\nThis is a placeholder text for error message in action_109\n"""
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()


@seq9.declare_action
def action_110(tb):
    """\nThis is a placeholder text for error message in action_110\n"""
    tb.deactivate(Input(1))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    tb.nothing_else_changes()


@seq9.declare_action
def action_111(tb):
    """\nThis is a placeholder text for error message in action_111\n"""
    tb.deactivate(Input(3))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(9))
    tb.nothing_else_changes()


seq10 = Sequence(10, "Test of ready to go signal")


@seq10.declare_action
def action_112(tb):
    """\nThis is a placeholder text for error message in action_112\n"""
    tb.activate(Input(5))
    tb.is_pulsing(Output(7), 1)
    tb.is_pulsing(Output(8), 1)
    tb.is_pulsing(Output(182), 1)
    tb.is_pulsing(Output(181), 1)
    tb.nothing_else_changes()


@seq10.declare_action
def action_113(tb):
    """\nThis is a placeholder text for error message in action_113\n"""
    tb.deactivate(Input(5))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    tb.nothing_else_changes()
