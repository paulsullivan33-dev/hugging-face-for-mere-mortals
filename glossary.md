# Glossary

**Blob** — in the cache, the actual
bytes of a downloaded file, stored
once under a hash name; snapshot
folders link to blobs (chapter 5).

**Cache** — the folder, by default
`~/.cache/huggingface`, where
downloads wait for reuse; the reason
second runs are fast (chapter 5).

**Checkpoint** — a saved state of a
model, usually just its weights at
some point in training; used loosely
for "a downloadable model file".

**Datasets (the shelf)** — the Hub's
collection of published data:
examples with labels, organised in
rows and splits (chapter 7).

**Fine-tune** — a model produced by
training an existing model further,
usually on narrower data for a
narrower job (chapter 1).

**Gated** — a repository whose files
are released only to accounts that
agree to the maker's terms
(chapter 9).

**GGUF** — the single-file format for
llama.cpp and its family, with
quantisation baked in (chapter 3).

**Hub** — Hugging Face's hosting
service: models, datasets and
Spaces under `owner/name` addresses
(chapter 1).

**Inference** — running a trained
model to get an answer, as opposed
to training it. Most of this guide
is inference's supply chain.

**Licence** — the legal terms a
model or dataset is published under;
part of the download, not fine
print (chapter 2).

**Model** — files that let a program
do one kind of AI job: chiefly a
large set of numbers, plus the small
files that describe them (chapter 1).

**Model card** — a model's page on
the Hub: description, licence,
intended use, data, results
(chapter 2).

**Parameters** — the individual
numbers in the weights; models are
sized by them (7B = seven billion)
(chapter 2).

**Pickle** — Python's object-saving
format underneath old `.bin` weight
files; loading one can run code,
which is why it is handled with
suspicion (chapter 3).

**Pipeline** — the transformers
library's one-call front door: give
it a job name and a model, get
answers (chapter 6).

**Quantisation** — storing weights in
fewer bits so the file shrinks,
trading a little quality for a lot
of size (chapter 3).

**Repository (repo)** — one item's
folder on the Hub, addressed
`owner/name`; a Git repository under
the skin (chapters 1, 11).

**Revision** — one specific version
of a repository, named by a commit
hash; pinning one makes a download
repeatable (chapter 5).

**safetensors** — the weight format
that holds numbers only and cannot
carry code; the safe default
(chapter 3).

**Space** — a small web app on the
Hub demonstrating a model, run on
Hugging Face's machines (chapter 10).

**Split** — a named slice of a
dataset: usually train, validation
and test (chapter 7).

**Token** — one piece of text from a
tokenizer's dictionary; the unit
models read, count, and bill by
(chapter 8).

**Tokenizer** — the program and
dictionary that turn text into
tokens and back; a matched pair with
its model (chapter 8).

**trust_remote_code** — the switch
that lets a model load its
publisher's Python code along with
its weights. Off is the correct
default; chapter 9 explains why this
guide never turns it on.

**Weights** — the learned numbers
themselves; the big file in every
model repository (chapters 1, 3).
