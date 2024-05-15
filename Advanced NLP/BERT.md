# Bidirectional Encoder Representation from Transformers (BERT)

Problems to solve
- Neural Machine Translation
- Question Answering
- Sentiment Analysis
- Text summarization

How to solve problems
- Pre-train BERT to understand language
- Fine-tune BERT to learn specific task

## Pre-training
- Learns what is language? what is context?
- This is done through masked language modelling (takes a sentence with random words filled with masks). The goal is to output the correct tokens. This helps BERT in understanding the language in bidirectional context
- It also uses Next Sentence Prediction where two sentences are taken and it determines whether the second sentence follows the first sentence. It helps in understanding the context between sentences

## Fine-tuning 
- How to use language for a specific task?
- Replace the fully connected output layers by the output layers that give the answer to the question we want
- Only minor changes are done and hence, the training time is fast
