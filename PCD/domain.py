from enum import IntEnum


class Input(IntEnum):

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


class Output(IntEnum):

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
