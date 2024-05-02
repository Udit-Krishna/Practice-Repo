# Bag of Words

Let sample sentences be
1. He is a good boy
2. She is a good girl
3. Boy and Girl are good

### Make all the letter cases and remove stopwords. Now the sentences become

1. good boy
2. good girl
3. boy girl good

```
Vocabulary      Frequency
good            3
boy             2
girl            2 
```
are sorted in descending order of frequency


Now, the vector features are chosen from the above table
```
            good    boy     girl
sentence 1  1       1       0
sentence 2  1       0       1
sentence 3  1       1       1
```
Therefore, the vectors of each sentences are S1 : [1,1,0], S2 : [1,0,1], S3 : [1,1,1]

Binary BoW has only 0s and 1s
BoW has numbers according to the frequency of the word in the sentence

### Advantages
1. Simple to implement and Intuitive
2. Fixed size input which is suitable for ML algorithms

### Disadvantages
1. Sparse matrix or array (0s and 1s) which leads to overfitting 
2. Order of the sentence is getting changed, which leads to change in meaning
3. Out of vocabulary (OOV) is still a problem
4. Semantic meaning is not captured

