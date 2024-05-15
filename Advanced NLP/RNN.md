# Deep Learning - NLP

1. RNN
2. LSTM RNN
3. GRU RNN
4. Bidirectional LSTM RNN
5. Encoders-Decoders
6. Transformers
7. BERT

<br>

# Recurrent Neural Networks (RNN)

1. One to One RNN - Image classification, 
2. One to Many RNN - Music generation, Text generation, google search and movie recommendation
3. Many to One RNN - Sentiment analysis, Predict next day sales
4. Many to Many RNN - Language translation, Question answering, chat bots

## Forward Propagation
- The weight is multiplied with the embedded inputs
- The output of the RNN, multiplied by a weight, is given as the input of the next RNN ( + the weight multiplied by the second embedded inputs)
- The cycle continues till we get the final output  

## Backward Propagation
- Updated weights = old weights - (learning rate - derivative of loss)
- derivative of loss can be found by applying chain rule on derivative of weight function

## Vanishing/Exploding Gradients Problem
- When the RNN is deep, weight updation will be vanishing if the weights for the ouput is much less than 1
- When the RNN is deep, weight updation will be explosive if the weights for the ouput is greater than 1
- To overcome this problem, we use LSTM (Long Short Term Memory) Networks
