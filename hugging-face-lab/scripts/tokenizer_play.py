#!/usr/bin/env python3
"""Chapter 8: watch a tokenizer chop text into tokens.

Uses the tokenizer that belongs to chapter 6's model
(uncased: it lowercases everything, and its dictionary
holds 30,522 entries).
"""
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)

print("vocab size:", tok.vocab_size)
print("special tokens:", tok.special_tokens_map)
print()

for text in [
    "Tokenizers are unreasonably effective",
    "The Unassuming Alpaca rearranged 14,208 paperclips.",
    "for shelf in shelves: print(shelf.name)",
]:
    pieces = tok.tokenize(text)
    ids = tok.convert_tokens_to_ids(pieces)
    print(f"text:   {text}")
    print(f"pieces: {pieces}")
    print(f"ids:    {ids}")
    print(f"count:  {len(pieces)} tokens for "
          f"{len(text.split())} words")
    print()

full = tok("Tokenizers are unreasonably effective")
print("with furniture, the model actually sees:")
print(" ", full["input_ids"])
print(" ", tok.convert_ids_to_tokens(full["input_ids"]))
