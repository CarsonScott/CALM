# Conditional-Associative Logic Memory

## Learning
The following is an unsupervised machine-learning algorithm that recognizes and predicts input patterns in real-time. The algorithm is essentially a system of information-processing inspired by the cognitive functions of the mind. The system has a collection of interacting memory systems akin to the spychological concepts of short-term and long-term memory, which allows it to learn by observation and adapt based on the frequency of patterns and their relationships through time. 

An association value is a representation of conditional probability which is calculated between the current observation and the rest of the elements in the buffer, i.e. the previous N observations, then stored in the association matrix. Each  elements current place in the buffer determines the strength of the delta applied to its association value, so more recent observation are more strongly associated with the current observations than those further in the buffer. The association matrix enables the prediction of future observations based on current and previous observations. A significantly large association for the current observation to another signify that the other is likely to occur. The association value indicates the strength of the connection as well as the confidence interval related to the prediction. 

Therefore a system may be understood in terms of a Bayesian network, whose adaptations inherently create a foundation for inference, as well as provide a useful data structure, i.e. directed/labeled associations, which can be used to construct higher level objects like sequences (chains of associations) used to represent episodic memory, which in turn combine to form trees (hierarchies of sequences) used for high level reasoning like considering various alternatives in case a planned action fails, or for creating recursive models of observations that span multiple levels of complexity.

## Prediction 
The system makes predictions based on the current and previous observations. It takes the rows of the association matrix that correspond the with elements currently stored in the buffer and calculates a probability distribution over the possible events that could occur at the next observation. Each probability depends on the current observation as well as the previous N observations, and therefore accomplishes a type of chaining that emphasizes the context of the observation to have an impact when inferring about the future.

## Examples [To be updated]
The following example was produced by selecting an observation at random from a set of 15 possible obervations. Each time a selection is ade, there is a small chance that the observation will not be random but instead will be from a "pattern", a pair of observations representing some event to be learned. The sampling process is repeated 1000 times and processed by the system to generate an association matrix.

    Pattern 1: {6, 13}
    Pattern 2: {9, 4)
    Pattern 3: {1, 5}
    
 ![](https://github.com/CarsonScott/AutoMLN/blob/master/img/Figure_1.png)

Each pairing of x and y coordinates represent an association from an x element to a y element. The z axis contains the association values for each pairing. Each peak represents a statistically significant association between two obserbation

