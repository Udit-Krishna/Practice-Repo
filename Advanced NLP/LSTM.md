# Long Short Term Memory (LSTM)

## Vanishing/Exploding Gradients Problem in RNN
- When the RNN is deep, weight updation will be vanishing if the weights for the ouput is much less than 1
- When the RNN is deep, weight updation will be explosive if the weights for the ouput is greater than 1
- To overcome this problem, we use LSTM (Long Short Term Memory) Networks

## How LSTM work?
- Instead of using the same feedback loop connection for both the events that happened long ago and short ago, we use two different feedback loop paths
- Cell state component - represents the long term memory without any weights and biases - hence, no modification
- Short term memory components have weights and biases that can modify them
- (FORGET GATE) The first stage of a LSTM determines what percent of the long term memory is remembered - Sigmoid Activation Function
- (INPUT GATE) In second stage, one block combines the short term memory and input to create a *potential long-term memory* - Sigmoid Activation Function. Another block determines what percentage of that *potential memory* to add to the long-term memory - Tanh activation function
- (OUTPUT GATE) Final stage updates the short term memory. Newly updated long term memory is used as input to the Tanh activation function. Now what percentage of this is to be remembered is determined similar to the first stage using a sigmoid function

