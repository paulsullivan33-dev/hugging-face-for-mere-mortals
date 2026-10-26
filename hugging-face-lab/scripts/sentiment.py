#!/usr/bin/env python3
"""Chapter 6: a model in three lines, plus a few extra tries.

The pipeline call names the job and the model. The first run
downloads the model into the Hub cache (about 270 MB); later
runs read it from there.
"""
from transformers import pipeline

reader = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

sentences = [
    "A small, kind film that knows exactly what it is doing.",
    "I waited an hour for a bus that never came.",
    "The meeting is on Tuesday at ten.",
    "The soup was neither hot nor cold, and somehow both.",
]

for sentence in sentences:
    print(f"{sentence!r}\n  -> {reader(sentence)[0]}")
