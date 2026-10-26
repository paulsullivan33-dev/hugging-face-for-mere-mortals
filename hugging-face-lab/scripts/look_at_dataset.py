#!/usr/bin/env python3
"""Chapter 7: load a tiny public dataset and look at it.

rotten_tomatoes: short film-review excerpts, each labelled
positive or negative. About a megabyte on disk.
"""
from datasets import load_dataset

ds = load_dataset("cornell-movie-review-data/rotten_tomatoes")
print(ds)
print()
print("features:", ds["train"].features)
print()
for row in ds["train"].select(range(3)):
    print(row)
print()
print("first validation row:", ds["validation"][0])
print("label counts (train):", 
      {name: sum(1 for x in ds["train"]["label"] if x == i)
       for i, name in enumerate(ds["train"].features["label"].names)})
