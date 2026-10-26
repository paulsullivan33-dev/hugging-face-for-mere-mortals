# Pipelines, a Model in Three Lines

**Outcome: you run a real model on
sentences of your own and read its
answers — and you know exactly what
the three lines did.**

The **transformers** library's front
door is the **pipeline**: one call
that names a job and a model, and
returns a working tool for that job.
The lab's whole script
(`hugging-face-lab/scripts/sentiment.py`)
is, at its heart:

```python
from transformers import pipeline

reader = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)
print(reader("A small, kind film."))
```

Unpack what those lines quietly did,
because it is most of the guide in
miniature:

- **The job name comes first.**
  `sentiment-analysis` is the task:
  read text, judge its feeling.
  Pipelines exist for dozens of jobs —
  transcription, translation,
  summarising, answering questions
  about a passage, labelling pictures.
  The job name decides what shape of
  answer comes back.
- **The model is named in full.**
  Chapter 2 exists because of this
  argument. A pipeline called *without*
  a model silently chooses a default —
  possibly large, possibly not the one
  whose card you read. Naming it is
  the habit that keeps chapter 14's
  longest entry from being about you.
- **The first run fetches, then works.**
  Given the name, the library looks in
  the cache (chapter 5), downloads
  whatever is missing — for this model,
  a 268 MB safetensors file (chapter
  3's prefer-this format) plus its
  tokenizer files — loads the weights,
  and only then answers. The lab's
  transcript t04 keeps the whole first
  run, fetch included; every run after
  it starts from the cache in seconds.

The answer is a small piece of data:
a **label** (`POSITIVE` or `NEGATIVE`)
and a **score** between 0 and 1 — the
model's confidence, not a percentage
of correctness. A score of 0.99 is the
model being sure; whether it is
*right* is a question the score cannot
answer, which is why the lab's script
feeds it four sentences, not one:
a clear compliment, a clear complaint,
one flat statement of fact, and one
deliberately slippery sentence. Read
the transcript and watch what the
model does with the last two. A model
with only two labels must choose one
for a sentence that has no feeling
at all — and does, confidently. That
is not a bug in this model. It is the
shape of every classifier, and the
reason chapter 13 insists that a
downloaded model is an instrument,
not an oracle.

The model itself deserves its honest
sentence: DistilBERT is a small,
elderly-by-field-standards reader
(2019's design, shrunk from a larger
model), fine-tuned on film reviews.
On film-flavoured sentences it is
good. On yours, it is a first
instrument to learn the machinery
with — which was the job it was
hired for here.

Check: run the script, then change
one sentence to something from your
own week — a headline, a product
description, a line from an email
you may share with a machine — and
predict the answer before it prints.
Being wrong teaches the same lesson
as the slippery sentence, in the
first person.
