from enum import Enum


class Input(Enum):

    # Power input
    POWER = 0

    # General inputs

    # IN_1 (from TC)
    CENTRAL_CLOSING_OF_DOORS = IN_1 = 1

    # IN_4 (from TC)
    BLOCKING_OF_DOORS = IN_4 = 4

    # IN_5 (from TC)
    READY_TO_GO = IN_5 = 5

    # in_16 (from pushbutton)
    MANUAL_OPERATION = IN_16 = 16

    # Inputs that has to do with the left side of train

    # IN_3 (from TC)
    FREEGIVING_OF_DOOR_L = IN_3 = 3

    # IN_9 (from sensor)
    LIMIT_STOP_DOOR_L = IN_9 = 9

    # IN_11 (from sensor)
    LIMIT_STOP_FOOTBOARD_L = IN_11 = 11

    # IN_13 (from mandrel-keycontact)
    LOCAL_OPERATION_DOOR_L = IN_13 = 13

    # IN_14 (from pushbutton)
    CLOSE_DOOR_L = IN_14 = 14

    # IN_15 (from pushbutton)
    OPEN_DOOR_L = IN_15 = 15

    # Inputs that has to do with the right side of train

    # IN_2 (from TC)
    FREEGIVING_OF_DOOR_R = IN_2 = 2

    # IN_6 (from pushbutton)
    CLOSE_DOOR_R = IN_6 = 6

    # IN_7 (from pushbutton)
    OPEN_DOOR_R = IN_7 = 7

    # IN_8 (from sensor)
    LIMIT_STOP_DOOR_R = IN_8 = 8

    # IN_10 (from sensor)
    LIMIT_STOP_FOOTBOARD_R = IN_10 = 10

    # IN_12 (from mandrel-key contact)
    LOCAL_OPERATION_DOOR_R = IN_12 = 12


class Output(Enum):

    # General output

    # OUT_3 (to TC)
    ACKNOWLEDGE_FOR_FREEGIVING_OF_DOORS = OUT_3 = 3

    # Outputs that has to do with the left side of train

    # OUT_2 (to TC)
    DOOR_CLOSED_L = OUT_2 = 2

    # OUT_5 (to buzzer)
    ATTENTION_SIGNAL_DOOR_LEFT = OUT_5 = 5

    # OUT_8 (to lamp)
    FLASH_LIGHT_L = OUT_8 = 8

    # OUT_9 (to lamp)
    OPENING_LIGHT_FOR_PUSHBUTTON_L = OUT_9 = 9

    # OUT_10 (to lamp)
    CLOSING_LIGHT_FOR_PUSHBUTTON_L = OUT_10 = 10

    # OUT_11 (to lamp)
    LIGHT_FOR_LOCAL_OPERATION_L = OUT_11 = 11

    # OUT_15 (To Pneumatic solenoid valve)
    OPEN_DOOR_L = OUT_15 = 15

    # OUT_171 (to Pneumatic solenoid valve)
    EMERGENCY_OPENING_BLOCKED_DOOR_L = OUT_171 = 171

    # OUT_181 (to lamp)
    LIGHT_FOR_CLOSING_OF_DOORS_L = OUT_181 = 181

    # OUT_19 (to Pneumatic solenoid valve)
    CLOSE_DOOR_L = OUT_19 = 19

    # Outputs that has to do with the right side of train

    # OUT_1 (to TC)
    DOOR_CLOSED_R = OUT_1 = 1

    # OUT_4 (to buzzer)
    ATTENTION_SIGNAL_DOOR_RIGHT = OUT_4 = 4

    # OUT_7 (to lamp)
    FLASH_LIGHT_R = OUT_7 = 7

    # OUT_12 (to lamp)
    OPENING_LIGHT_FOR_PUSHBUTTON_R = OUT_12 = 12

    # OUT_13 (to lamp)
    LIGHT_FOR_LOCAL_OPERATION_R = OUT_13 = 13

    # OUT_14 (to lamp)
    CLOSING_LIGHT_FOR_PUSHBUTTON_R = OUT_14 = 14

    # OUT_16 (to Pneumatic solenoid valve)
    OPEN_DOOR_R = OUT_16 = 16

    # OUT_172 (to Pneumatic solenoid valve)
    EMERGENCY_OPENING_BLOCKED_DOOR_R = OUT_172 = 172

    # OUT_182 (to lamp)
    LIGHT_FOR_CLOSING_OF_DOORS_R = OUT_182 = 182

    # OUT_20 (to Pneumatic solenoid valve)
    CLOSE_DOOR_R = OUT_20 = 20


class TestBoxPrinter:

    # ask user to do actions on input

    def activate(self, contact):
        if contact.value == 0:
            print(f"\nActivate {contact.name} contact.\n")
        else:
            print(f"\nActivate contact IN {contact.value} ({contact.name}).\n")

    def deactivate(self, contact):
        print(f"\nDeactivate contact IN {contact.value} ({contact.name}).\n")

    def pulse(self, contact, time):
        print(f"\nActivate contact IN {contact.value}", end=' ')
        print(f"({contact.name})", end=' ')
        print(f"and turn it off after {time} second.\n")

    # ask user to check on output

    def is_active(self, output, time=None):
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
        print(f"Is every output unaltered ?")

    # get answers from user

    def wait_for_input(self):

        active = [int(x)
                  for x in
                  input("List answers for the questions: ").split(",")
                  ]
        print(active)


# Power-on test

def action_1(tb):
    tb.activate(Input(0))  # Input(0) = Input.POWER
    tb.is_active(Output(1))  # Input(1) = Input.IN_1
    tb.is_active(Output(2))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    # tb.wait_for_input()


# Test of right doorside

def action_2(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    # tb.wait_for_input()


def action_3(tb):
    tb.pulse(Input(7), 1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_4(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_5(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_6(tb):
    tb.pulse(Input(6), 1)
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    # tb.wait_for_input()


def action_7(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.nothing_changes()
    # tb.wait_for_input()


def action_8(tb):
    tb.pulse(Input(7), 1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_9(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.nothing_changes()
    # tb.wait_for_input()


def action_10(tb):
    tb.pulse(Input(6), 1)
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    # tb.wait_for_input()


def action_11(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.nothing_changes()
    # tb.wait_for_input()


def action_12(tb):
    tb.deactivate(Input(2))
    tb.is_active(Output(1))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(13))
    # tb.wait_for_input()


def action_13(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    # tb.wait_for_input()


def action_14(tb):
    tb.pulse(Input(7), 1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_15(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_16(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_17(tb):
    tb.deactivate(Input(2))
    tb.is_pulsing(Output(13), 3)
    # tb.wait_for_input()


def action_18(tb):
    tb.pulse(Input(6), 1)
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    # tb.wait_for_input()


def action_19(tb):
    tb.activate(Input(8))
    tb.is_pulsing(Output(1), 1)
    # tb.wait_for_input()


def action_20(tb):
    tb.activate(Input(10))
    tb.is_active(Output(1))
    # tb.wait_for_input()


def action_21(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    # tb.wait_for_input()


def action_22(tb):
    tb.pulse(Input(7), 1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_23(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_24(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_25(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(9))
    # tb.wait_for_input()


def action_26(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_27(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_28(tb):
    tb.pulse(Input(14), 1)
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    # tb.wait_for_input()


def action_29(tb):
    tb.activate(Input(9))
    tb.is_pulsing(Output(2), 1)
    # tb.wait_for_input()


def action_30(tb):
    tb.activate(Input(11))
    tb.is_active(Output(2))
    # tb.wait_for_input()


def action_31(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(9))
    # tb.wait_for_input()


def action_32(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_33(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_34(tb):
    tb.deactivate(Input(2))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    tb.is_pulsing(Output(13), 3)
    # tb.wait_for_input()


def action_35(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    # tb.wait_for_input()


def action_36(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(20))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(13))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    # tb.wait_for_input()


def action_37(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    # tb.wait_for_input()

# Test of left doorside


def action_38(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    tb.wait_for_input()
    # tb.wait_for_input()


def action_39(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_40(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_41(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_42(tb):
    tb.pulse(Input(14), 1)
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    # tb.wait_for_input()


def action_43(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.nothing_changes()
    # tb.wait_for_input()


def action_44(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_45(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.nothing_changes()
    # tb.wait_for_input()


def action_46(tb):
    tb.pulse(Input(14), 1)
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    # tb.wait_for_input()


def action_47(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.nothing_changes()
    # tb.wait_for_input()


def action_48(tb):
    tb.deactivate(Input(3))
    tb.is_active(Output(2))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(11))
    # tb.wait_for_input()


def action_49(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    # tb.wait_for_input()


def action_50(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_51(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_52(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_53(tb):
    tb.deactivate(Input(3))
    tb.is_pulsing(Output(11), 3)
    # tb.wait_for_input()


def action_54(tb):
    tb.pulse(Input(14), 1)
    tb.is_active(Output(19))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(15))
    # tb.wait_for_input()


def action_55(tb):
    tb.activate(Input(9))
    tb.is_pulsing(Output(2), 1)
    # tb.wait_for_input()


def action_56(tb):
    tb.activate(Input(11))
    tb.is_active(Output(2))
    # tb.wait_for_input()


def action_57(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    # tb.wait_for_input()


def action_58(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_59(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_60(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_61(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(12))
    # tb.wait_for_input()


def action_62(tb):
    tb.pulse(Input(7), 1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_63(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_64(tb):
    tb.pulse(Input(6), 1)
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    # tb.wait_for_input()


def action_65(tb):
    tb.activate(Input(8))
    tb.is_pulsing(Output(1), 1)
    # tb.wait_for_input()


def action_66(tb):
    tb.activate(Input(10))
    tb.is_active(Output(1))
    # tb.wait_for_input()


def action_67(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(12))
    # tb.wait_for_input()


def action_68(tb):
    tb.pulse(Input(7), 1)  # Input(7) = Input.IN_7
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_69(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_70(tb):
    tb.deactivate(Input(3))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    tb.is_pulsing(Output(11), 3)
    # tb.wait_for_input()


def action_71(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    # tb.wait_for_input()


def action_72(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(19))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(11))
    tb.is_inactive(Output(15))
    # tb.wait_for_input()


def action_73(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    # tb.wait_for_input()


def action_74(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    # tb.wait_for_input()


def action_75(tb):
    tb.activate(Input(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    # tb.wait_for_input()


def action_76(tb):
    tb.pulse(Input(7), 1)
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_77(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_78(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_79(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_80(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_81(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(11))
    # tb.wait_for_input()


def action_82(tb):
    tb.deactivate(Input(2))
    tb.deactivate(Input(3))
    tb.is_pulsing(Output(11), 3)
    tb.is_pulsing(Output(13), 3)
    # tb.wait_for_input()


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
    # tb.wait_for_input()


def action_84(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    # tb.wait_for_input()


def action_85(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    # tb.wait_for_input()


def action_86(tb):
    tb.activate(Input(16))
    tb.is_inactive(Output(172))
    tb.is_inactive(Output(171))
    tb.is_inactive(Output(19))
    tb.is_inactive(Output(20))
    tb.is_pulsing(Output(1), 1)
    tb.is_pulsing(Output(2), 1)
    # tb.wait_for_input()


def action_87(tb):
    tb.deactivate(Input(8))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_88(tb):
    tb.deactivate(Input(9))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_89(tb):
    tb.activate(Input(8))
    tb.activate(Input(9))
    tb.is_pulsing(Output(1), 1)
    tb.is_pulsing(Output(2), 1)
    # tb.wait_for_input()


def action_90(tb):
    tb.deactivate(Input(16))
    tb.is_active(Output(1))
    tb.is_active(Output(2))
    tb.is_active(Output(172))
    tb.is_active(Output(171))
    tb.is_active(Output(19))
    tb.is_active(Output(20))
    # tb.wait_for_input()


def action_91(tb):
    tb.deactivate(Input(4))
    tb.is_inactive(Output(172))
    tb.is_inactive(Output(171))
    # tb.wait_for_input()


def action_92(tb):
    tb.activate(Input(2))
    tb.is_active(Output(3))
    tb.is_active(Output(12))
    tb.is_active(Output(4), 4)
    # tb.wait_for_input()


def action_93(tb):
    tb.activate(Input(7))
    tb.is_active(Output(14))
    tb.is_active(Output(16))
    tb.is_inactive(Output(12))
    tb.is_inactive(Output(20))
    # tb.wait_for_input()


def action_94(tb):
    tb.deactivate(Input(8))
    tb.deactivate(Input(10))
    tb.is_inactive(Output(1))
    # tb.wait_for_input()


def action_95(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(13))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_96(tb):
    tb.activate(Input(1))
    tb.is_pulsing(Output(7), 5)
    tb.is_pulsing(Output(8), 5)
    tb.is_pulsing(Output(182), 5)
    tb.is_pulsing(Output(181), 5)
    # tb.wait_for_input()


def action_97(tb):
    tb.pulse(Input(12), 1)
    tb.is_active(Output(3))
    tb.is_inactive(Output(13))
    tb.is_pulsing(Output(14), 5)
    # tb.wait_for_input()


def action_98(tb):
    tb.pulse(Input(6), 1)
    tb.is_active(Output(12))
    tb.is_active(Output(20))
    tb.is_inactive(Output(14))
    tb.is_inactive(Output(16))
    # tb.wait_for_input()


def action_99(tb):
    tb.activate(Input(8))
    tb.activate(Input(10))
    tb.is_active(Output(1))
    # tb.wait_for_input()


def action_100(tb):
    tb.deactivate(Input(1))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    # tb.wait_for_input()


def action_101(tb):
    tb.deactivate(Input(2))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(12))
    #  tb.wait_for_input()


def action_102(tb):
    tb.activate(Input(3))
    tb.is_active(Output(3))
    tb.is_active(Output(9))
    tb.is_active(Output(5), 4)
    # tb.wait_for_input()


def action_103(tb):
    tb.pulse(Input(15), 1)
    tb.is_active(Output(10))
    tb.is_active(Output(15))
    tb.is_inactive(Output(9))
    tb.is_inactive(Output(19))
    # tb.wait_for_input()


def action_104(tb):
    tb.deactivate(Input(9))
    tb.deactivate(Input(11))
    tb.is_inactive(Output(2))
    # tb.wait_for_input()


def action_105(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(11))
    tb.is_pulsing(Output(3), 1)
    # tb.wait_for_input()


def action_106(tb):
    tb.activate(Input(1))
    tb.is_pulsing(Output(7), 5)
    tb.is_pulsing(Output(8), 5)
    tb.is_pulsing(Output(182), 5)
    tb.is_pulsing(Output(181), 5)
    # tb.wait_for_input()


def action_107(tb):
    tb.pulse(Input(13), 1)
    tb.is_active(Output(3))
    tb.is_inactive(Output(11))
    tb.is_pulsing(Output(10), 5)
    # tb.wait_for_input()


def action_108(tb):
    tb.pulse(Input(14), 1)
    tb.is_active(Output(9))
    tb.is_active(Output(19))
    tb.is_inactive(Output(10))
    tb.is_inactive(Output(15))
    # tb.wait_for_input()


def action_109(tb):
    tb.activate(Input(9))
    tb.activate(Input(11))
    tb.is_active(Output(2))
    # tb.wait_for_input()


def action_110(tb):
    tb.deactivate(Input(1))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    # tb.wait_for_input()


def action_111(tb):
    tb.deactivate(Input(3))
    tb.is_inactive(Output(3))
    tb.is_inactive(Output(9))
    # tb.wait_for_input()


def action_112(tb):
    tb.activate(Input(5))
    tb.is_pulsing(Output(7), 1)
    tb.is_pulsing(Output(8), 1)
    tb.is_pulsing(Output(182), 1)
    tb.is_pulsing(Output(181), 1)
    # tb.wait_for_input()


def action_113(tb):
    tb.deactivate(Input(5))
    tb.is_inactive(Output(7))
    tb.is_inactive(Output(8))
    tb.is_inactive(Output(182))
    tb.is_inactive(Output(181))
    # tb.wait_for_input()


if __name__ == "__main__":
    tb = TestBoxPrinter()
    action_1(tb)
    #  action_2(tb)
    action_11(tb)
    #  action_5(tb)

    # tb.wait_for_input()
