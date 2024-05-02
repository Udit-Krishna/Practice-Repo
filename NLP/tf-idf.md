# TF-IDF Term Frequency - Inverse Document Frequency

- If the word is present in all the paragraphs, it is given less importance



Let sample sentences be
1. good boy
2. good girl
3. boy girl good


Term Frequency TF = No. of repetition of words in sentence / No. of words in sentence

Inverse Document Frequency IDF = log<sub>e</sub>(No. of sentences/No. of sentences containing the word)

Term Frequency table
```
        S1      S2      S3
good    1/2     1/2     1/3
boy     1/2     0       1/3
girl    0       1/2     1/3
```
Inverse Document Frequency table
```
        IDF
good    loge(3/3)=0
boy     loge(3/2)
girl    loge(3/2)
```

Final TF-IDF
```
                good            boy                 girl
sentence 1      0               1/2*loge(3/2)       0
sentence 2      0               0                   1/2*loge(3/2)     
sentence 3      0               1/3*loge(3/2)       1/3*loge(3/2)   
```

### Advantages
1. Intuitive
2. Fixed size input (based on vocab size)
3. Word importance is getting captured

### Disadvantages
1. Sparsity still exists
2. Out of Vocabulary is still a problem
