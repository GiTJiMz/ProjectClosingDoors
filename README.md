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

- Modules in Package PCD<br><br/>
  
    - **\_\_main__.py**
      > **In this module I run my program with an interactive line-oriented command interpreter.\
      This is where the repair man gets to choose whether he wants to test a specific door-function\
      or test all of it.**
      
    - **actions.py**
      > **In this module I have all my actions which is carried out on the testbox.\
      All the actions are grouped under sequences which represent the different door-functions.**
      
    - **domain.py**
      > **In this module I have all my inputs and outputs.\
      Input and output are used in the actions, as these consist of input that is affected and output that must be verified.**
      
    - **printer.py**
      > **In this module I have all the directions / instructions which is printed / written to the repairman\
      in every action.**
      
    - **statemachine.py**
      > **This module is run separately and writes all the states that the testbox is going through.\
      Besides of that this module is generating the commands for representing the state machine as a directed graph.\
      The graph can be visualized via the commands with a graph visualization software like graphviz.\
      E.g. on this link: http://www.webgraphviz.com/ the digraph commands can be pasted directly in to the field
      and generate a graph. For my statemachine it looks like this:**
    
    
![Image of PCD state machine](PCD/State_machine.png)

## Explanation of code

- ### General
  
  - pass

- ### Advanced programming technique vs data structure
  
  - General purpose languages (GPL) like Python, C # etc. are often difficult to talk about and evaluate and semantics are often difficult to understand
    because they are SO general purpose and can do so many things.<br><br/>

    Therefore, you have something called Domain Specific Language (DSL) which means that you build a new programming language
    which only takes care of things in one's own domain.
    A DSL then gives, among other things, the advantage that you do not risk being hacked as much, as you have limited the possibilities, in your own language, for e.g. to have methods exploited by hackers to do damage to the system.
    This also makes it safer and easier to understand due to the limitation.<br><br/>
    
    Examples of DSL are SQL, HTML, plantUML and even DOT which is a language used to describe graphs.<br><br/>
    
    It is anything but just easier to write both HTML and SQL commands than if you had to use a GPL to program yourself out of it with loops and various programming techniques that you had to type each time.<br><br/>
    
    It is quite complicated to make a DSL, as you have to make parsers and syntax highlighter and many other things that should make it easy to use.<br><br/>
    
    So instead you can make use of the syntax of a host language to give new semantics, so you just avoid having to build your own syntax tree, parser and syntax highlighter and so on.<br><br/>
    
    When you use the host language to give new semantics, you embed the DSL in the host language which in our case is Python.
    DSLs created in this way are called eDSL (embedded Domain Specific Language).<br><br/>
    
    In my project, I have created an eDSL, which is an advanced programming technique, for my domain.<br><br/>
    
    The eDSL itself is in fact the description of my actions in the host language (Python).
    The evaluator is the output or the effect you want in the end and I can interpret the output in 2 different ways, namely my test box printer that makes my system interactive and the state machine that represents all states of the test box.
    In order to write my actions I have described all inputs and outputs and it is part of the domain specific language (DSL).<br><br/>
    
    The state machine is a type of graph with direction that shows how to get from one state to another state.
    And the graph, which is an advanced data structure, I will have to examine more in the future to see if the test can be optimized.

- ### Exciting stuff
  
  - #### Decorator
    
    I thought decorators are super exciting, so here I will show how I have used it in my code.<br><br/>
    I have taken 3 code snippets that illustrate the use of the decorator.<br><br/>
    In the first code snippet I have the class Sequence and here I want to highlight the method declare_action which works as the decorator.<br><br/>
    This link highlights the decorator.

    https://github.com/GiTJiMz/ProjectClosingDoors/blob/99ff5f09429f88748d0aca10517bdcb0dce9adb3/PCD/actions.py#L13-L15
    <br><br/>
    
    In the next code snippet, I instantiate an object of class 'Sequence'.<br><br/>
    
    In the last piece of code, I use the @ operator to decorate the desired function.<br><br/>

    In my case, I decorate my actions with the method declare_action for the specific instance which is a sequence that in turn represents a door function.<br><br/>

    The line with the code '@ seq3.declare_action' calls the method declare_action on the sequence object 'seq3'
    with the function 'def action_21 (tb)' as parameter.
    Here the function is added to the list 'actions' for the sequence object.<br><br/>

    All the actions where I put the code '@ seq3.declare_action' just above the action are grouped under the same sequence / door function (seq3).

```python
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
```

```python
      seq3 = Sequence(3, "Test of service-access in left doorside (e.g. to fill up catering)")
```

```python
      @seq3.declare_action
      def action_21(tb):
          """\nThis is a placeholder text for error message in action_21\n"""
          tb.activate(Input(2))
          tb.is_active(Output(3))
          tb.is_active(Output(12))
          tb.is_active(Output(4), 4)
          tb.nothing_else_changes()
```

- ### Defects and deficiencies
  
  - #### Defects
    
    When the repairman chooses to run a full test, the actions action_power_off, action_start_position and action_1 are run every time a new door function / sequence starts.<br><br/>
    The right thing is that the 3 actions only have to run once, and it has to happen just before the first door function is run.<br><br/>
    Therefore, the text "Testing: Door-function 1: Test of local operation of right door [11]" must also be moved down so that it's above the text
    "Testing: action_2", if you answer yes and thus confirm the correctness of the questions in action_1.
    
  - #### Deficiencies

    1. The repairer must be able to choose how many times a test should be repeated.<br><br/>
    2. In the vast majority of actions, only one input is stimulated, but there are also some actions where 2 inputs are stimulated.<br><br/>
       Therefore, after stimulation of each input in the actions, all outputs must be checked so that the error messages can become very specific and thus shorter.<br><br/>
       Currently it's the repairman who has to stimulate the inputs and answer the questions, and therefore it's only more work for the person in question, but in return it helps to pinpoint the error.<br><br/>
       The idea is that the test box will be replaced, in the future, by a hardware interface that automates the test. So it would facilitate the programming of the hardware interface, later, if it was implemented in the current test box printer.<br><br/>
    3. In this version of the program, error message is only entered for one action (action_2 in door function 1), so error messages for 112 actions are missing.<br><br/>
    4. The error messages must be stored permanently in a file where the repairmen can easily enroll new help for other repairmen.
       From here, the help can be read into the program at startup.<br><br/>
    5. The code for the state machine has only just been made, and I have generated the image of the graph, but I have not been able to deduce anything from it yet.\
       So I will definitely move on with this in the future and see if it's possible to run the test in a more efficient way without compromising on quality.


## Conclusion

It has been a steep learning curve, as I have both had to get to know Python at the same time as a lot of new concepts.

It has been a good process with very valuable communication with the teacher and fellow students.
This has contributed to me modulating my domain in a good way.

There are mistakes that need to be corrected and there is room for improvement, but it's a completely natural part when working with the development of your product.

Going forward, I will put energy into interpreting on the state machine in order to streamline the test as well as
to figure out how I want to check all outputs after stimulating each input. I think the remaining shortcomings are going to be more affordable to implement.

After this project, I am now left with a product, in the form of a program that we can use at work, as a replacement for the current testing regulation.

I am extremely pleased with the process and the result.