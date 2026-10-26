# File Formats in Plain Terms

**Outcome: you can look at a model's
file list and say what each file is,
which ones can hurt you, and how big
the download really is.**

A model's repository is a folder of
files, and the filenames carry almost
all the information. Four kinds of
file do nearly all the work, plus a
handful of small text files that
travel with every model.

## The weights, in their three coats

The big file is the **weights**: the
numbers the model learned. The same
numbers are published in different
**formats**, and the format decides
which programs can load the model and
how much you should trust the file.

**safetensors** — files ending
`.safetensors`. The modern default,
and the one to prefer. The format
holds numbers and nothing else: a
short header describing each block of
numbers (its name, its shape, where
it sits in the file), then the
numbers themselves. There is nowhere
in it for code to hide, so loading a
safetensors file cannot run anything.
It also loads fast, because a program
can map the file and read only the
parts it needs. When a repository
offers a choice, this is the choice.

**PyTorch bin** — files ending `.bin`,
usually `pytorch_model.bin`, sometimes
split into numbered shards. The older
format. Underneath, it is a **pickle**,
Python's own way of saving objects —
and a pickle is a small program that
rebuilds the object when loaded, which
means a hostile `.bin` file can run
code on your machine at load time.
This is not a theoretical crack: it
is the format's design. The Hub scans
uploads for known-bad pickles and
shows the result on the page
(chapter 9), and makers have largely
moved to safetensors — but where a
`.bin` is all that is offered, treat
it as you would treat running a
stranger's script, because that is
closer to what it is.

**GGUF** — files ending `.gguf`. A
single-file format built for
**llama.cpp** and the tools around it
(including Ollama, chapter 12): the
weights, already **quantised**
(squeezed, next section), with the
model's settings packed into the same
file. One file, one download, runs
on ordinary CPUs. If a repository
name ends in `-GGUF`, it is a shelf
of these files at different squeezes,
and you pick exactly one.

**ONNX** — files ending `.onnx`, a
portable format for moving models
between frameworks, common for
production and edge devices. You
will meet it in the wild; this
guide's lab does not use it.

## Quantisation, and the names decoded

**Quantisation** means storing each
weight in fewer bits — rounding the
numbers to a coarser scale so the
file shrinks and the arithmetic gets
faster, at a small cost in quality.
A model's raw size is easy maths:
**parameters × bytes each**. Seven
billion parameters at full two-byte
precision is about 14 GB. At one byte
each, about 7 GB. Quantised to an
average of roughly half a byte each,
about 3.5 to 4 GB — which is why the
squeezed files are the ones that fit
on home machines.

GGUF filenames carry the recipe in
the name. Take a real pattern:

```text
model-8b.Q4_K_M.gguf
```

Read it left to right: the model,
its size class (8B), then the
quantisation code **Q4_K_M**:

- **Q4** — about 4 *bits* per weight
  on average (roughly a quarter of
  the two-byte original's size).
- **K** — a "K-quant", a scheme that
  squeezes the less sensitive numbers
  harder than the sensitive ones,
  rather than treating all alike.
- **M** — medium, within its family:
  the size/quality middle of the
  Small–Medium–Large choices offered
  for that recipe.

Other codes you will meet: **Q8_0**
(8 bits, barely squeezed, near
original quality, half the size),
**Q5_K_S** and **Q5_K_M** (5 bits,
the quality sweet spot for many),
**Q3** and **Q2** (aggressively
small, visibly dumber — a way to fit
a too-big model, not a free lunch),
**F16** (not quantised: the original
two-byte numbers), and **IQ** names
("importance" quants, a newer scheme
that decides what to preserve using
a calibration pass). The pattern is
the thing to keep: *smaller number,
smaller file, dumber model* — and
the file size on the card always
settles arguments the name starts.

## The small files that travel along

Every repository also carries small
text files, kilobytes each, without
which the big file is a brick:

- `config.json` — the model's
  blueprint: how many layers, how
  wide, what kind of model it is.
  Programs read this first.
- The **tokenizer** files
  (`tokenizer.json`, `vocab.txt` or
  `tokenizer.model`, and friends) —
  the dictionary that turns text into
  numbers and back (chapter 8). A
  model and its tokenizer are a
  matched pair; never borrow one from
  another model.
- `generation_config.json` — the
  maker's suggested settings for
  producing text: how random, when
  to stop.
- `README.md` — the model card
  itself, chapter 2.
- Sometimes `*.py` files — actual
  code the model needs. This is the
  one that matters for trust: loading
  such a model asks you to run the
  publisher's code, and the tools make
  you say so explicitly
  (chapter 9, and never say it
  lightly).

Check: open any large model's Files
tab and decode three filenames aloud
— format, quantisation, size — then
find the tokenizer files. If the
weights exist in both `.bin` and
`.safetensors`, you already know
which one a careful person fetches.
