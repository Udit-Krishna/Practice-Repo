# Word2Vec

- Uses a neural network to learn word associations from a large corpus of text
- Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence
- Represents each distinct word with a particular list of numbers called as **vectors**


Example of Feature Representation of the vocabulary: Boy, Girl, King, Queen, Apple, Mango....

```
        Boy     Girl    King    Queen   Apple   Mango
Gender  -1       1     -0.92    0.93    0.01    0.02
Royal   0.01    0.02    0.95    0.96   -0.02    0.02 
Age     0.03    0.02    0.75    0.68    0.92    0.91
Food                                    0.95    0.96
.
.
nth
```

KING - BOY + QUEEN = GIRL can be solved by used these vector representation of the words

<br>

### Cosine Similarity
- Used to find the similarity between two vectors using the angle between them
- Distance = 1 - cosine similarity
- Cosine similarity = cosine of the angle between the two vectors

<br>

```
            Word2Vec
              / \
             /   \
            /     \
  Pre-trained    Train from Scratch
```
<br><br><br>

## Continuous Bag of Words (CBoW)
- The whole corpus (dataset) is split into segments of window size = n
- The middle word of the window is considered as the output
- Other words are considered as the input
- Middle word is chosen so that we can capture both forward and backward association
- All the words are one hot encoded
- All the one hot encoded segments are taken as the input for a fully connected neural network
- The hidden layer has number of vectors equal to the window size
- The output layer has number of vectors equal to the output vector length
- All nodes are connected to each other in the network
- The neural network is trained to find the predicted output
- The predicted output is compared with the actual output using loss function
- Backward propagation is carried out to minimize the loss function
- <font color="red">THE WINDOW SIZE IS EQUAL TO THE OUTPUT WORD VECTOR SIZE</font>

<br><br>

## Skipgram
- Major difference between Skipgram and CBoW is that the input is the middle word and the output are the forward and backward associated words

<br><br>

## When to apply CBoW and Skipgram?
- Small datasets, use CBoW
- Huge datasets, use Skipgram

<br>

For better results,
- Increase dataset size
- Increase the window size which leads to increase of vector dimensions

<br><br>

## Google Word2Vec 
- 3 billion words
- Feature representation of 300 dimensions