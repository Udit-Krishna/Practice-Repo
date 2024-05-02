# One Hot Encoding

- Assigns one for each word and zero for other words
- Creates a two-dimensional array for each sentence
- The sub array contains the one hot encoding of the word


For example: Let the vocabulary be [the, food, is, good, bad, pizza, amazing]
For a sentence: the food is bad, the One hot encoding version would be
[[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,1,0,0]]

### Advantages
- Easy to implement in Python (Using sklearn OneHotEncoder or pandas.get_dummies)

### Disadvantages
- Sparse matrix - causing overfitting
- Machine algorithms require fixed size input, but this encoding provides output with different lengths according to the length of the word
- The semantic meaning of the sentence is not captured
    - For example, it is not possible to find the relationship between words using this encoding method
- Out of vocabulary (OOV) words cannot be handled
