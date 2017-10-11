# AutoMLN


## Overview
The system observes a set of inputs and calculates a matrix describing associations between elements of the input. The association value between two elements ranges from 1 to -1, or very related to not related at all. A network that contains each input element and their connections calculates the weight of a connection from the association value between the two elements.

An element becomes active in one of two ways. The first is through the input set, which contains a boolean value for each element. Nonzero input values cause the associated elements to become active. The second way is through the network, which allows weighted signals to pass between connected elements and influence their activity. An element becomes active when the total value from its connections is greater than its threshold. As activity passes from element to element, the signal becomes weaker and weaker until it fails to activate any further elements. 
