from transformers import pipeline  

import sys
import os

gpt2 = pipeline('text-generation', model = "./poem_gene/sequential_generator")  


def generate_with_start_str(start_str: str, num_return_sequences: int = 6):
    sequences = gpt2(f'<|endoftext|>{start_str}', max_length=34, do_sample=True, top_k=20, top_p=0.9,
                      num_return_sequences=num_return_sequences, eos_token_id=0)
    for i in range(len(sequences)):
        sequences[i] = sequences[i]['generated_text'].replace(' ', '')[13:]
    for i in reversed(range(len(sequences))):
        if len(sequences[i]) != 32:
            sequences.pop(i)
    while len(sequences) < num_return_sequences:
        sequences += generate_with_start_str(start_str, num_return_sequences - len(sequences))
    return sequences

# if __name__ == '__main__':
#     seqs = generate_with_start_str('雨过')
#     for seq in seqs:
#         print(seq)