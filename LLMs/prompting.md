# Prompting and Prompt Engineering

## In-Context Learning (ICL)
- Zero shot inference
    - No examples given in prompt
    - Takes less space in context window
    - Might not produce good results
- One shot inference
    - One example given in prompt
    - Takes a bit more space in context window than zero shot
    - Might produce satisfactory results
- Few shot inference
    - Multiple examples given in prompt
    - Context window size might be an issue
    - Produces good results

<br><br> 

## Generative configuration

### Greedy vs Random Sampling
- In greedy sampling, the word/token with the highest probability is selected
- In random (or weighted) sampling, select a token using a random-weighted strategy across
the probabilities of all tokens. 

### Parameters:
- Max new tokens
    - Maximum number of tokens generated during inference
- Top K
    - Select an output from the top-k results after applying random-weighted strategy using the probabilities
- Top P
    - Select an output using the random-weighted strategy with the top-ranked consecutive results by probability and with a cumulative probability <= p.
- Temperature
    - Randomness of the output
    - Cooler temperature (<1) have a strongly peaked probability distribution
    - Higher temperature (>1) have a broader and flatter probability distribution
