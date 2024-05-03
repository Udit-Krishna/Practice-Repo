# Generative AI - Introduction

- They take prompt as input
- Produce completion as output
- Context window refers to the maximum size of the input that the model can take as input

## LLM Use cases and tasks
- Essay writing
- Summarization
- Translation
- Information Retrieval
- Invoke APIs and actions

## Why RNNs don't work properly
- They do not capture the meaning of the sentence properly
- Understanding Languages can be challenging through RNNs
- Parallel processing is not possible, serial processing takes a long time

## Transformers
- They scale efficiently
- Can be processed in parallel
- Gives attention to input meaning
- Finds the relationship between all the words in the sentence through self-attention

<br>

They consist of
- Encoder
- Decoder
- Embedding for both encoder and decoder
- Softmax output layer after the decoder

<br><br>

**Process of Embedding**:
- The input words are tokenized before providing to the embedding layer - each word is identified with a token ID (Token Embedding)
- Embedding does positional encoding where the information about the relative position of each token within the sequence is captured (Position Embedding)
- In the embed space, synonyms and similar words are situated closer while the antonyms and different words are located further
- This embedded tokens are provided as input for both encoder and decoder blocks for further processing

<br><br>

**Multi-headed Self Attention in Encoder and Decoder**
- A single self-attention mechanism might struggle to capture all the important relationships within a sequence.
- Multi-headed self-attention addresses this by introducing multiple independent "heads" that learn different aspects of the relationships between elements.
- Each head performs a similar attention calculation but with its own set of learnable parameters.

### Encoder and Decoder
- Encoder encodes prompts with contextual understanding and produces one vector per input tokens
- Decoder accepts tokens and generate new tokens

### Types of Transformers
- Encoder only Models
- Encoder Decoder Models
- Decoder only Models
