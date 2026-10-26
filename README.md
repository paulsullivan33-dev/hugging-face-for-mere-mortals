# Hugging Face for Mere Mortals

Somewhere there is a shelf where nearly
every open AI model lives, and most
tutorials eventually tell you to take
something down from it: *download this
model, load that dataset*. **Hugging
Face** runs the shelf — the **Hub** —
and this guide teaches you to use it
with your eyes open: what a **model**
actually is when it arrives (a large
file of numbers, a few small files,
and a **licence**), how to read the
**model card** before fetching
anything, how to tell **safetensors**
from **GGUF** from an old pickle in a
`.bin` coat, how the **`hf` command
line** and its cache work, and how to
run a small model and open a small
dataset for real.

The rule that governs everything here
is stated in chapter 1: **read the
card, check the licence, and download
only what you are willing to be
responsible for running.** A downloaded
model is other people's code and data
landing on your machine under terms
you accepted by taking it. That is
not a reason to stay away from the
shelf. It is a reason to learn the
shelf properly, which is a morning's
work and is this book.

The lab behind this guide ran the real
thing, with no account and no
credentials: **huggingface_hub 2.3.0**,
**transformers 5.20.2** and
**datasets 5.1.0**, installed with pip
into a fresh virtual environment on a
small Linux machine. With them it
fetched a two-megabyte toy model with
the `hf` command and took the cache
apart to see where the files live; read
three models' cards as data —
licences, file lists, sizes —
including one **gated** model, whose
files it then politely failed to
download, exactly as the fence intends;
ran a real sentiment model on four
sentences and watched it judge a flat
statement of fact with total
confidence; opened a dataset of film
reviews and counted its rows, splits
and labels; pulled a tokenizer apart
to see how a sentence becomes numbers;
and ran the model a second time with
the network switched off, from the
cache alone.

What the lab could not do without an
account, it did not fake. Publishing
models, datasets and Spaces, accepting
a gated model's terms, and running
publisher-supplied code
(`trust_remote_code`) are described
from the documentation and labelled
as such wherever they appear; this
guide never created an account and
never flipped that switch.
`criteria.md` keeps the full ledger
of what was run and what was only
read.

## What this guide covers

- [**What Hugging Face is**](what-hugging-face-is.md) —
  the Hub, its three shelves (models,
  datasets, Spaces), the `owner/name`
  address everything wears, and the
  rule about downloads being other
  people's work
- [**Reading a model card**](reading-a-model-card.md) —
  the card as a contract: licence,
  intended use, training data, results,
  and the Files tab read before any
  download starts
- [**File formats in plain terms**](file-formats.md) —
  safetensors, PyTorch `.bin` and its
  pickle, GGUF, quantisation, and
  decoding a name like `Q4_K_M`
- [**Installing the tools**](installing-the-tools.md) —
  the pip install into a virtual
  environment, the CPU-build question,
  and the checks that prove the tools
  answer
- [**The hf command line**](the-hf-cli.md) —
  downloading whole repositories or
  single files, the cache taken apart
  (blobs, snapshots, refs), and
  working offline
- [**Pipelines, a model in three lines**](pipelines.md) —
  a sentiment model run for real, what
  the pipeline quietly fetched, and
  how to read a label and a score
- [**Datasets, loading and looking**](datasets.md) —
  loading a dataset, its splits and
  features, counting rows and labels,
  and looking before you load
- [**Tokenizers**](tokenizers.md) —
  how text becomes numbers: tokens,
  dictionaries, special marks, and why
  length and cost are counted in
  tokens, not words
- [**Judging what to trust**](judging-trust.md) —
  verified owners, cards as evidence,
  file inventories, scan results,
  gated fences, and popularity's false
  testimony
- [**Spaces**](spaces.md) — the Hub's
  showroom floor: demos that run on
  their machines, what visiting one
  sends and risks, in outline
- [**Sharing your own work**](sharing-your-work.md) —
  publishing models, datasets and
  Spaces, the card you owe your
  readers, and the licence you sign —
  described, not performed
- [**The neighbours**](the-neighbours.md) —
  the Ollama library, Civitai, the
  vendors' own pages, Kaggle: the same
  models in other wrappings, and other
  transactions entirely
- [**Limits**](limits.md) — a shelf is
  not a guarantee, models inherit
  their data, size is a wall, licences
  bind, and things move and vanish
- [**Troubleshooting**](troubleshooting.md) —
  the sudden login demand, the missing
  repository, the empty offline cache,
  the pickle warning, and the traps
  this guide's lab fell into so you
  don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Training a model from scratch, or
fine-tuning technique in depth — this
is a guide to the shelf, not the
kitchen; the shelf's own documentation
is the next step for both. Running
the very large models is bounded by
chapter 13's arithmetic and your
machine, not by anything a guide can
lend you. Inference at production
scale — serving models to many users
— is pointed at, not taught. And
getting *around* a gate, a licence,
or a publisher's terms is not a
harder chapter of this book; chapter
9 explains why the fence is the part
of the deal that was for you.

## How to use this guide

Read chapter 1 for the model of the
place and chapter 2 before downloading
anything at all — the card-reading
habit is the skill the rest of the
book spends. Chapters 4 and 5 install
the tools and take the cache apart;
do them in one sitting, with the toy
model, while nothing is large enough
to be precious. Chapters 6 to 8 run
one model, one dataset and one
tokenizer, and are worth doing with
the scripts in front of you
(`hugging-face-lab/scripts/`); the
transcripts (`hugging-face-lab/transcripts/`)
are the lab's own runs, kept so you
can compare your output against a
known one. Chapter 9 is not the
optional chapter: run its checks on
the next model anyone recommends to
you. The lab's notes are
`examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Local AI for Mere Mortals](https://paulsullivan33-dev.github.io/local-ai-for-mere-mortals/)
- [llama.cpp for Mere Mortals](https://paulsullivan33-dev.github.io/llama-cpp-for-mere-mortals/)
- [Ollama for Mere Mortals](https://paulsullivan33-dev.github.io/ollama-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/hugging-face-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/hugging-face-for-mere-mortals/blob/main/LICENSE-CODE).
