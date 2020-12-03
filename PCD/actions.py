from PCD.domain import Input, Output


class Sequence:
    instances = {}

    def __init__(self, id: int, description="", actions=None):
        self.id = id
        self.description = description
        self.actions = actions or []
        Sequence.instances[id] = self

    def declare_action(self, action):
        # actions[action.__name__] = action
        self.actions.append(action)
        return action

    def run(self, tb):
        for action in self.actions:
            action(tb)

    def __str__(self):
        return f"Door-function {self.id}: {self.description} " \
               + f"[{len(self.actions)}]"


# Start position

def action_start_position(tb):
    tb.activate(Input(8))
    tb.activate(Input(9))
    tb.activate(Input(10))
    tb.activate(Input(11))
    # tb.deactivate_all_other_input()
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    # tb.everything_else_deactivated()


# Power-on test

def action_1(tb):
    tb.activate(Input(0))  # Input(0) = Input.POWER
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    # tb.nothing_else_changes()


# Test of right door side

seq1 = Sequence(1, "Test of local operation of right door")


@seq1.declare_action
def action_2(tb):
    tb.activate(Input(2))  # Input(2) = Input.IN_2
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_3(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_4(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_5(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_6(tb):
    tb.pulse(Input(6))
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_7(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.nothing_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_8(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_9(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.nothing_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_10(tb):
    tb.pulse(Input(6))
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_11(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.nothing_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq1.declare_action
def action_12(tb):
    tb.deactivate(Input(2))
    tb.is_active(Output(1))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(13))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq2 = Sequence(2, """Test of attention signal to TGF,
                   when right door is local operated
                   and acknowledge for freegiving of doors
                   is deactivated.
                   The door closed signal for right door is also tested""")


@seq2.declare_action
def action_13(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_14(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_15(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_16(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_17(tb):
    tb.deactivate(Input(2))
    tb.is_pulsing(Output(13), 3)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_18(tb):
    tb.pulse(Input(6))
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_19(tb):
    tb.activate(Input(8))
    tb.is_pulsing(Output(1), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq2.declare_action
def action_20(tb):
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq3 = Sequence(3, "Test of service-access in left doorside (e.g. to fill up catering)")


@seq3.declare_action
def action_21(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_22(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_23(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_24(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_25(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(9))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_26(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_27(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_28(tb):
    tb.pulse(Input(14))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_29(tb):
    tb.activate(Input(9))
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_30(tb):
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_31(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(9))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_32(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_33(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_34(tb):
    tb.deactivate(Input(2))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.is_pulsing(Output(13), 3)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_35(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_36(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq3.declare_action
def action_37(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


# Test of left door side

seq4 = Sequence(4, "Test of local operation of left door")


@seq4.declare_action
def action_38(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_39(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_40(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_41(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_42(tb):
    tb.pulse(Input(14))
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_43(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.nothing_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_44(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_45(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.nothing_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_46(tb):
    tb.pulse(Input(14))
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_47(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.nothing_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq4.declare_action
def action_48(tb):
    tb.deactivate(Input(3))
    tb.is_active(Output(2))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(11))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq5 = Sequence(5, """Test of attention signal to TGF,
                   when left door is local operated
                   and acknowledge for freegiving of doors
                   is deactivated.
                   The door closed signal for left door is also tested""")


@seq5.declare_action
def action_49(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_50(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_51(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_52(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_53(tb):
    tb.deactivate(Input(3))
    tb.is_pulsing(Output(11), 3)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_54(tb):
    tb.pulse(Input(14))
    tb.is_active(Output(19))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_55(tb):
    tb.activate(Input(9))
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq5.declare_action
def action_56(tb):
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq6 = Sequence(6, "Test of service-access in left doorside (e.g. to fill up catering)")


@seq6.declare_action
def action_57(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_58(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_59(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_60(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_61(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(12))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_62(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_63(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_64(tb):
    tb.pulse(Input(6))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_65(tb):
    tb.activate(Input(8))
    tb.is_pulsing(Output(1), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_66(tb):
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_67(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(12))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_68(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_69(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_70(tb):
    tb.deactivate(Input(3))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.is_pulsing(Output(11), 3)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_71(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_72(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(19))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq6.declare_action
def action_73(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq7 = Sequence(7, "Test of blocking of doors and manual operation")


@seq7.declare_action
def action_74(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_75(tb):
    tb.activate(Input(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_76(tb):
    tb.pulse(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_77(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_78(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_79(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_80(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_81(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_82(tb):
    tb.deactivate(Input(2))
    tb.deactivate(Input(3))
    tb.is_pulsing(Output(11), 3)
    tb.is_pulsing(Output(13), 3)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_83(tb):
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
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_84(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_85(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_86(tb):
    tb.activate(Input(16))
    tb.is_inactive(Output(172))
    tb.is_inactive(Output(171))
    tb.is_inactive(Output(19))
    tb.is_inactive(Output(20))
    tb.is_pulsing(Output(1), 1)
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_87(tb):
    tb.deactivate(Input(8))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_88(tb):
    tb.deactivate(Input(9))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_89(tb):
    tb.activate(Input(8))
    tb.activate(Input(9))
    tb.is_pulsing(Output(1), 1)
    tb.is_pulsing(Output(2), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_90(tb):
    tb.deactivate(Input(16))
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(172))
    tb.is_active(Output(171))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq7.declare_action
def action_91(tb):
    tb.deactivate(Input(4))
    tb.is_inactive(Output(172))
    tb.is_inactive(Output(171))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq8 = Sequence(8, "Test of central closing of doors, when right door is local operated")


@seq8.declare_action
def action_92(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_93(tb):
    tb.activate(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_94(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_95(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_96(tb):
    tb.activate(Input(1))
    tb.is_pulsing(Output(7), 5)
    tb.is_pulsing(Output(8), 5)
    tb.is_pulsing(Output(182), 5)
    tb.is_pulsing(Output(181), 5)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_97(tb):
    tb.pulse(Input(12), 0.5)
    tb.is_active(Output(3))
    tb.is_inactive(Output(13))
    tb.is_pulsing(Output(14), 5)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_98(tb):
    tb.pulse(Input(6))
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_99(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_100(tb):
    tb.deactivate(Input(1))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq8.declare_action
def action_101(tb):
    tb.deactivate(Input(2))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(12))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq9 = Sequence(9, "Test of central closing of doors, when left door is local operated")


@seq9.declare_action
def action_102(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_103(tb):
    tb.pulse(Input(15))
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_104(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_105(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_106(tb):
    tb.activate(Input(1))
    tb.is_pulsing(Output(7), 5)
    tb.is_pulsing(Output(8), 5)
    tb.is_pulsing(Output(182), 5)
    tb.is_pulsing(Output(181), 5)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_107(tb):
    tb.pulse(Input(13), 0.5)
    tb.is_active(Output(3))
    tb.is_inactive(Output(11))
    tb.is_pulsing(Output(10), 5)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_108(tb):
    tb.pulse(Input(14))
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_109(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_110(tb):
    tb.deactivate(Input(1))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq9.declare_action
def action_111(tb):
    tb.deactivate(Input(3))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(9))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


seq10 = Sequence(10, "Test of ready to go signal")


@seq10.declare_action
def action_112(tb):
    tb.activate(Input(5))
    tb.is_pulsing(Output(7), 1)
    tb.is_pulsing(Output(8), 1)
    tb.is_pulsing(Output(182), 1)
    tb.is_pulsing(Output(181), 1)
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)


@seq10.declare_action
def action_113(tb):
    tb.deactivate(Input(5))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    tb.nothing_else_changes()
    # answer = tb.wait_for_input()
    # return tb.treat_input(answer)
