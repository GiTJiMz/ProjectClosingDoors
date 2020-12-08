# ProjectClosingDoors

## Problem statement / objective

The electronics department, in DSB electrical engineering, tests and repairs the electronics in DSB's train equipment.

The door control for the IC3 train is tested by a repairman who tests all functions, by connecting a test box to the door control and carefully carrying out everything that is stated in the test regulations.

The test regulations contain 113 points and the repairman must perform all the points, on the test box, in the order in which they are written. Each point is called an action and tells exactly which inputs, in the form of contacts, the repairman must manually influence and how the outputs must react.

When the test is run, it is very long and trivial and you have the feeling that you do the same thing all the time.

The risk of making mistakes in the test is great when testing manually in this way and with so many actions. Furthermore, one can easily be disturbed and forget where one had come to, in the test regulations, and risk jumping back to a previous action. It takes approx. 30-45 minutes to get through the entire test regulation. If the test fails, the repairman must now repair the fault, and the same time is again consumed when testing the door control from scratch, if you want to be sure that there are no other faults.
or that new faults have been introduced during the repair.

So the ultimate goal is to get the test automated by executing the test regulation via a hardware interface (e.g. Raspberry pi), with code written in Python. When the test finds faults, it must stop and give hints to the repairman in connection with troubleshooting and repair.

It brings down the time and eliminates the possibility of errors in performing the test.

### Boundary:

The final goal cannot be achieved within the given deadline, so the project is limited to a sub-goal.

The sub-goal is to make the test box as a printer, in Python, understood in the sense that when the actions are performed on the test box, the test box writes / prints the instruction to the repairman, who must perform the action on the test box that exists today. When the repairman has influenced the input, it must also be answered whether the output is correct in the given action, so that it is also part of the instruction. If there is an error, the repairman will receive an error message.

The 113 actions are grouped into door functions, so that the repairman can in practice choose whether all or a specific door function is to be tested.

That way, the product ends up being an interactive test where the test box asks the repairman to perform the actions. The intention is to eventually replace the test box printer with the hardware interface that automatically performs the actions
and tells if there are errors or not.

The test / test box is also a state machine that again takes the form of a graph.

So I have chosen to make a graph for the test / test box, in order to see if there are many repetitions and if the test can be performed smarter.

## Organization / structure

- Modules in Package PCD
    - \_\_main__.py
      > In this module I run my program with an interactive line-oriented command interpreter.\
      This is where the repair man gets to choose whether he wants to test a specific door-function\
      or test all of it.
    - actions.py
      > In this module I have all my actions which is carried out on the testbox.\
      All the actions are grouped under sequences which represent the different door-functions.
    - domain.py
    - printer.py
    - statemachine.py