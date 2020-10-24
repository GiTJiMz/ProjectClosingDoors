from enum import Enum

class Button(Enum):
    POWER = 0
    OPEN_DOOR_L = 1
    
class Output(Enum):
    DOOR_CLOSED_R = 1
    CLOSING_LIGHT_L = 10
    OPEN_DOOR_L = 15
    OPENING_LIGHT_L = 9
    CLOSE_DOOR_L = 19


class TestBoxPrinter:
    
    # actions on input
    
    def activate(self, button):
        print(f"Activate button {button}.")
    
    def deactivate(self, button):
        print(f"")
        
    def pulse(self, button, time):
        print(f"Activate {button} and turn off {button} after {time} second")
    
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
    tb.activate(Button.POWER)
    tb.is_active(Output.DOOR_CLOSED_R)
    
def action_32(tb):
    tb.pulse(Button.OPEN_DOOR_L, 1)
    tb.is_active(Output.CLOSING_LIGHT_L)
    tb.is_active(Output.OPEN_DOOR_L)
    tb.is_inactive(Output.OPENING_LIGHT_L)
    tb.is_inactive(Output.CLOSE_DOOR_L)
    tb.wait_for_input()

if __name__ == "__main__":
    tb = TestBoxPrinter()
    action_32(tb)
    # action_1(tb)
    # tb.wait_for_input()