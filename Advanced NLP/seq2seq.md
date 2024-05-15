# Encoder-Decoder Neural Networks (Seq2Seq)

- One type of sequence can be translated to another type of sequence using this network. For example: Language translation
- Need to handle variable length inputs and outputs



## Encoder
- Uses embedding layer to convert the words into numbers. In the vocabulary (all the words used by the models), each word is known as token
- Has multiple LSTM layers with each layer having separate LSTM cells with their own weights and biases
- There are multiple LSTM layers to fit the training data
- The output of the first layer of LSTM is used as the input for the second layer of LSTM
- The last long and short term memories from the both layers of the LSTM cells in the encoder are called the Context vector
- Therefore the input is encoded into the Context vector by the Encoder

## Decoder
- The context vectors initialize the long and short term memories for the LSTM in the Decoder
- The LSTMs in the decoder have their own weights and biases different from the Encoder
- The embedding layer here creates embedding values for the target language tokens
- The outputs from the LSTM layers are transformed by additional weights and biases from a fully connected layer
- These fully connected layers have two inputs from the two outputs of the LSTM cells
- They have the outputs corresponding to the number of tokens in the vocabulary calculated with a softmax function
- However the decoder does not stop until it outputs an `<EOS>` token.
- Therefore, we send the outputs of the LSTM cells as the inputs to another layer of LSTM cells
- Using a fully connected layer, we predict the next token

## Training the Encoder-Decoder Model
- During training, we use backpropagation
- Although the output of the first layer of decoder is wrong, we use the correct token for the next layer of LSTM cells
- Instead of waiting for an `<EOS>` token during training, each output phrase ends where the known phrase ends
- These are known as **Teacher Forcing**
