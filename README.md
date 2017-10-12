# AutoMLN

### 1. Agents and Memory

1.1 __Overview__

An agent is a system of information processing inspired by the cognitive functions of the mind. Agents have a collection of interacting memory systems akin to the spychological concepts of short-term and long-term memory. Agents learn by observation and adapt based on the frequency of patterns and their relationships. The result is a knowledge-base with the capacity to recognize observations and predict future events.

1.2 __Encoding and Storage__

The system observes a set of inputs and calculates a matrix describing associations between elements of the input. The association value between two elements ranges from 1 to -1, or very related to not related at all. A network that contains each input element and their connections calculates the weight of a connection from the association value between the two elements.

1.3 __Retreival__

An element becomes active in one of two ways. The first is through the input set, which contains a boolean value for each element. Nonzero input values cause the associated elements to become active. The second way is through the network, which allows weighted signals to pass between connected elements and influence their activity. An element becomes active when the total value from its connections is greater than its threshold. As activity passes from element to element, the signal becomes weaker and weaker until it fails to activate anymore elements. 
