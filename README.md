# AutoMLN

## Overview

The following is an outline for an unsupervised machine-learning algorithm that recognizes and predicts input patterns in real-time. The algorithm is essentially a system of information-processing inspired by the cognitive functions of the mind. The system has a collection of interacting memory systems akin to the spychological concepts of short-term and long-term memory, which allows it to learn by observation and adapt based on the frequency of patterns and their relationships through time. 

An association value is a representation of conditional probability which is calculated between the current observation and the rest of the elements in the buffer, i.e. the previous N observations, then stored in the association matrix. Each  elements current place in the buffer determines the strength of the delta applied to its association value, so more recent observation are more strongly associated with the current observations than those further in the buffer. The association matrix enables the prediction of future observations based on current and previous observations. A significantly large association for the current observation to another signify that the other is likely to occur. The association value indicates the strength of the connection as well as the confidence interval related to the prediction. 

Therefore a system may be understood in terms of a Bayesian network, whose adaptations inherently create a foundation for inference, as well as provide a useful data structure, i.e. directed/labeled associations, which can be used to construct higher level objects like sequences (chains of associations) used to represent episodic memory, which in turn combine to form trees (hierarchies of sequences) used for high level reasoning like considering various alternatives in case a planned action fails, or for creating recursive models of observations that span multiple levels of complexity.

## Examples
The following example was produced by selecting an observation at random from a set of 15 possible obervations. Each time a selection is ade, there is a small chance that the observation will not be random but instead will be from a "pattern", a pair of observations representing some event to be learned. The sampling process is repeated 1000 times and processed by the system to generate an association matrix.

    Pattern 1: {6, 13}
    Pattern 2: {9, 4)
    Pattern 3: {1, 5}
    
 ![](https://github.com/CarsonScott/AutoMLN/blob/master/img/Figure_1.png)

Each pairing of x and y coordinates represent an association from an x element to a y element. The z axis contains the association values for each pairing. Each peak represents a statistically significant association between two obserbation

The X and Y axes each represent the set of elements, and the Z axis represents the association values. Each peak represents a pair of elements in the pattern. The trough running diagonally through the center are the associations between elements and themselves, equaL to -1 by default. The rest of the graph in blue represent statistically insignificant or random pairings of elements. 
