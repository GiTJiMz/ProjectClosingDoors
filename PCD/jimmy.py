from enum import Enum

class Input(Enum):
    #Power
    POWER = 0

    #General
    CENTRAL_CLOSING_OF_DOORS = 1            # IN_1 (from TC)
    BLOCKING_OF_DOORS = 4                   # IN_4 (from TC)
    READY_TO_GO = 5                         # IN_5 (from TC)
    MANUAL_OPERATION = 16                   # in_16 (from pushbutton)

    #Left
    FREEGIVING_OF_DOOR_L = 3                # IN_3 (from TC)
    LIMIT_STOP_DOOR_L = 9                   # IN_9 (from sensor)
    LIMIT_STOP_FOOTBOARD_L = 11             # IN_11 (from sensor)
    LOCAL_OPERATION_DOOR_L = 13             # IN_13 (from mandrel-key contact)
    CLOSE_DOOR_L = 14                       # IN_14 (from pushbutton)
    OPEN_DOOR_L = 15                        # IN_15 (from pushbutton)
    
    #Right
    FREEGIVING_OF_DOOR_R = 2                # IN_2 (from TC)
    CLOSE_DOOR_R = 6                        # IN_6 (from pushbutton)
    OPEN_DOOR_R = 7                         # IN_7 (from pushbutton)
    LIMIT_STOP_DOOR_R = 8                   # IN_8 (from sensor)
    LIMIT_STOP_FOOTBOARD_R = 10             # IN_10 (from sensor)
    LOCAL_OPERATION_DOOR_R = 12             # IN_12 (from mandrel-key contact)
    
class Output(Enum):
    
    #General
    ACKNOWLEDGE_FOR_FREEGIVING_OF_DOORS = 3 # OUT_3 (to TC)
    
    #Left
    DOOR_CLOSED_L = 2                       # OUT_2 (to TC)
    ATTENTION_SIGNAL_DOOR_LEFT = 5          # OUT_5 (to buzzer)
    FLASH_LIGHT_L = 8                       # OUT_8 (to lamp)
    OPENING_LIGHT_FOR_PUSHBUTTON_L = 9      # OUT_9 (to lamp)
    CLOSING_LIGHT_FOR_PUSHBUTTON_L = 10     # OUT_10 (to lamp)
    LIGHT_FOR_LOCAL_OPERATION_L = 11        # OUT_11 (to lamp)
    OPEN_DOOR_L = 15                        # OUT_15 (to Pneumatic solenoid valve)
    EMERGENCY_OPENING_BLOCKED_DOOR_L = 171  # OUT_171 (to Pneumatic solenoid valve)
    LIGHT_FOR_CLOSING_OF_DOORS_L = 181      # OUT_181 (to lamp)
    CLOSE_DOOR_L = 19                       # OUT_19 (to Pneumatic solenoid valve)

    #Right
    DOOR_CLOSED_R = 1                       # OUT_1 (to TC)
    ATTENTION_SIGNAL_DOOR_RIGHT = 4         # OUT_4 (to buzzer)
    FLASH_LEFT_R = 7                        # OUT_7 (to lamp)
    OPENING_LIGHT_FOR_PUSHBUTTON_R = 12     # OUT_12 (to lamp)
    LIGHT_FOR_LOCAL_OPERATION_R = 13        # OUT_13 (to lamp)
    CLOSING_LIGHT_FOR_PUSHBUTTON_R = 14     # OUT_14 (to lamp)
    OPEN_DOOR_R = 16                        # OUT_16 (to Pneumatic solenoid valve)
    EMERGENCY_OPENING_BLOCKED_DOOR_R = 172  # OUT_172 (to Pneumatic solenoid valve)
    LIGHT_FOR_CLOSING_OF_DOORS_R = 182      # OUT_182 (to lamp)

class TestBoxPrinter:

    # actions on input
    
    def activate(self, button):
        print(f"Activate button {button}.\n")
    
    def deactivate(self, button):
        print(f"Deactivate button {button}.\n")

    def pulse(self, button, time):
        print(f"Activate {button} and turn off {button} after {time} second.\n")
    
    # check on output

    def is_active(self, output):
        print(f"Is {output} active ?")
    
    def is_inactive(self, output):
        print(f"Is {output} inactive ?")

    def is_pulsing(self, output, frequency):
        print(f"Is {output} pulsing with {frequency} Hz ?")
        
    # user input

    def wait_for_input(self):
        active = [ int(x)
          for x in
          input("List answers for the questions: ").split(",")
          ]
        print(active)
    
def action_1(tb):
    tb.activate(Input.POWER)
    tb.is_active(Output.DOOR_CLOSED_R)

def action_32(tb):
    tb.pulse(Input.OPEN_DOOR_L, 1)
    tb.is_active(Output.CLOSING_LIGHT_FOR_PUSHBUTTON_L)
    tb.is_active(Output.OPEN_DOOR_L)
    tb.is_inactive(Output.OPENING_LIGHT_FOR_PUSHBUTTON_L)
    tb.is_inactive(Output.CLOSE_DOOR_L)
    tb.wait_for_input()

if __name__ == "__main__":
    tb = TestBoxPrinter()
    action_32(tb)

    # tb.wait_for_input()