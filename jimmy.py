from enum import Enum

class Button(Enum):
    POWER = 0
    
class Output(Enum):
    DOOR_CLOSED_H = 1

class TestBoxPrinter:
    
    def activate(self, button):
        print(f"Activate button {button}.")
        
    def pulse(self, button, time):
        pass
    
    def is_active(self, output):
        print(f"Check that {output} is active.")
    
    def is_inactive(self, output):
        print(f"Check that {output} is inactive.")
        
    def wait_for_input(self):
        active = [ int(x)
          for x in
          input("List active outputs").split(",")
          ]
        print(active)
    
    
def action_1(tb):
    tb.activate(Button.POWER)
    tb.is_active(Output.DOOR_CLOSED_H)
    
    
    
tb = TestBoxPrinter()

action_1(tb)
tb.wait_for_input()
    