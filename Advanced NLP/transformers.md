# Transformers -  Attention is all you need

- Does parallel processing instead of serial processing done by RNNs, LSTMs
- The word is embedded into numbers for the neural networks to work with them
- The weights and biases of the embedding layers are found out by backpropagation while training

## Positional Encoding
- A technique that transformers use to keep track of word order
- The embedded words are passed to positional encoders to create word embeddings with context information
- Word embeddings are created which are specific to the order of the words in the sentence

## Self Attention
- Works by seeing how similar each word is to all of the words in the sentence, including itself
- The similarity between words is calculated and is used to determine how the transformer encodes each word
- Multi headed attention layers are used to capture the attention of each word

## Decoder Block
- It works with the output words
- Embedding is done similar to the encoder block
- The outputs are passed on to the feed forward layers and the probability of next word is calculated using softmax function

## In a English-French translation
- Encoder learns what is english and what is the context
- Decoder learns how to map English words to French words
