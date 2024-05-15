# Encoder-Decoder + Attention in Neural Networks

- In a basic encoder-decoder model, the LSTMs compress the entire input sequence into a single context vector
- Although this works for smaller sentences, this will not work for longer sentences
- Hence, we have additional path (**Attention**) from each inputs so that the decoder has direct access to inputs
- Attention determines how similar the outputs from the Encoder LSTMs are at each step to the outputs of the Decoder LSTMs
- In other words, a similarity score is calculated between these embedded words using different methods.
- Some of the common methods are by using *cosine similarity*, and *dot product*
- These scores are then sent as input to the softmax function to determine what percentage of each encoded input word we should be using when decoding

