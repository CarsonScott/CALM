# AutoMLN

## Overview

The following is an outline for an unsupervised machine-learning algorithm that recognizes and predicts input patterns in real-time. An agent is a system of information processing inspired by the cognitive functions of the mind. Agents have a collection of interacting memory systems akin to the spychological concepts of short-term and long-term memory. Agents learn by observation and adapt based on the frequency of patterns and their relationships. The result is a knowledge-base with the capacity to recognize observations and predict future events.

![](https://github.com/CarsonScott/AutoMLN/blob/master/img/Memory.PNG)

The system receives a set of inputs and stores them in in a short-term memory unit called a buffer. It then Calculates a matrix describing associations between elements in the buffer. The association between two elements ranges from 1 to -1 regarding how related each element is with the other. A long-term storage unit called a network takes the association matrix and calculates a set of changes that are applied to the connections between elements. If two elements are stored in the buffer at the same time, their connection weight increases. If one is  in the buffer and the other is not, their connection weight decreases. 

When an element is active, the activation signal propagates to connected elements where it is multiplied by the connection weight. The sum of weighted signals received by an element is calculated to determine whether it becomes active. The total is compared to a threshold value and produces a new activation signal if it is larger than the threshold. Each time a signal is passed from one element to another, the magnitude of the signal decreases until it can no longer activates any further elements.
