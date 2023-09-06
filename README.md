# Llama Seance
Summon famous people to chat with using the Llama 2 LLM. Ever wanted to ask Shakespeare to write your cat a sonnet? Or discuss shipbuilding with Noah? Now you can.

## Requirements
- conda/miniconda CUDA environment with [Llama 2](https://github.com/facebookresearch/llama) installed
- either an RTX 4090 or a lot of patience

## Example
```
torchrun seance.py
  ...
The seance will now begin.
Who would you like to summon?
> William Shakespeare

What would you ask William Shakespeare?
> Please write a sonnet about my fat cat Charlie.

Knuckles crack, candles flicker, and curtains gently waft as the summoning begins...
17 seconds later William Shakespeare's ghostly voice is heard:

Oh, wondrous feline, Charlie, thou art a sight
To behold, with flabby cheeks and round, soft light
  ...
```