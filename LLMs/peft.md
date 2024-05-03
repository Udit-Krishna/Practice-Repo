# Parameter-efficient Fine-tuning (PEFT)

- Full fine-tuning of LLMs is challenging because they required too much memory to store the training weights, gradients, optimizer states, etc.

## PEFT
- Has small number of trainable layers
- Most of the layers of the LLM are frozen
- New trainable layers are added for PEFT
- Less prone to catastrophic forgetting since the original weights are untouched
- Unlike full fine-tuning which creates full copy of original LLM per task, PEFT fine-tuning saves space and more flexible by creating PEFT weights for each model which is at a considerably smaller size

## PEFT Methods
- Selective
    - Select a subset of initial LLM parameters to fine-tune
- Reparameterization
    - Reparameterize model weights using a low-rank representation
- Additive
    - Add trainable layers or parameters to model

## LoRA (Low Rank Adaptation of LLMs)
- Type of reparameterization method
- Freeze most of the original LLM weights
- Inject 2 rank decomposition matrices
- Train the weights of the smaller matrices
- This weight is then added to the original model weights
- For example:
    - Use the base Transformer model presented by Vaswani et al. 2017
        - Transformer weights have dimensions d x k = 512 x 64
        - So 512 x 64 = 32,768 trainable parameters
    - In LoRA with rank r = 8:
        - A has dimensions r x k = 8 x 64 = 512 parameters
        - B has dimension d x r = 512 x 8 = 4,096 trainable parameters
        - 86% reduction in parameters to train!