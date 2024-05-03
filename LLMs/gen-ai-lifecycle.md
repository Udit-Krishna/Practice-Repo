# Generative AI Project Lifecycle

1. Define the use case
    - Should the model be good at single task? or be good at multiple tasks?
2. Choose an existing model or pretrain your own
    - Autoencoding models (Encoder-only models)
        - Pretrained using Masked Language Modelling (MLM)
        - The tokens in the input sequence are randomly masked and the training objective is to predict the masked token
        - They build bidirectional representations of the input sequence (understand the full context of the token)
        - Suited for sentiment analysis, Named entity recognition, Word classification. 
        - Example Models: BERT, RoBERTa
    - Autoregressive models (Decoder-only models)
        - Pretrained using causal language modelling (CLM).
        - The training objective is the predict the next token based on the previous tokens
        - They mask the input tokens and can only see the input tokens leading up to the token in question
        - Iterate over the input sequence one by one to predict  the following token
        - Unlike Autoencoding models, Autoregressive models only have uni-directional context
        - Often used for Text Generation
        - Example models: GPT, BLOOM
    - Sequence-to-Sequence (Encoder-Decoder LLM)
        - Pretraining depends from model to model
        - T5 Encoder uses span correction which masks random sequences of input tokens, those masked sequences are replaced with sentinel token (special tokens added to the vocabulary)
        - The Decoder reconstructs the mask token sequences autoregressively
        - Often used for Translation, Text summarization, Question Answering
        - Example models: T5, BART

3. Adapt and align model:
    1. Prompt Engineering
        - Designing effective prompts to produce desired results
        - Using Zero shot, One shot or Few shot inferences
    2. Fine-tuning
        - Fine tuning on a single task
            - Use a training dataset to train the model
            - Can cause catastrophic forgetting where the model performs poorly on other tasks
            - To avoid catastrophic forgetting, fine tune for multiple tasks or consider Parameter Efficient Fine Tuning (PEFT)
        - Multi task instruction fine tuning
    3. Align with human feedback
4. Evaluate the model
    - Use metrics such as
        - Rogue: used for text summarization, compares one or more reference summaries
        - BLEU score: Used for text translation, compares for human-generated translations
5. Optimize and deploy model for inference
6. Augment model and build LLM-powered applications
