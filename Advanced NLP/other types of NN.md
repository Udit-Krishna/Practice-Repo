# Gated Recurrent Unit

- Newer and more efficient than LSTM
- Unlike RNN, it does not remember all the words 
- It only remembers the important key words
- LSTM has two memory (long and short term)
- GRU has both of them combined
- Has two gates - UPDATE and RESET
- UPDATE gate remembers how much of the past memory is to be retained
- RESET gate remembers how much of the past memory is to be forgotten

<br><br>

# Bidirectional RNN
- Traditional RNN only remembers the context of the word using the words before it
- In bidirecitonal, the context of the word depends on both the words that come before and the words that come afterwards
- There are two RNNs. One goes from start to end and another one goes from end to start
- Works great with NLP tasks because we have the entire sentence to begin with
- May not work well with speech recognition because we may not get the entire sequence to begin with
- Much slower compared to LSTM and RNN

