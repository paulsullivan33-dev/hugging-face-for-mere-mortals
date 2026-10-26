# What Hugging Face Is

**Hugging Face** is a company, and
**the Hub** is the thing it runs: a
public website where people publish
**models** — the files that make an AI
program able to do a job — along with
the **datasets** they were trained and
tested on, and small demonstration apps
called **Spaces**. If you have used a
local AI tool at all, you have probably
already eaten from this shelf: model
files all over the internet trace back
to a Hub page, usually without saying
so. This guide teaches you to read the
shelf directly.

An account is not required for anything
in the first eleven chapters. Looking
is free, and downloading anything
public is free. An account enters the
story only at the edges: models whose
owners ask you to agree to terms first
(chapter 9), and publishing work of
your own (chapter 11, which this guide
describes but does not do).

## The three shelves

Everything on the Hub sits on one of
three shelves, and the tabs at the top
of every page name them:

- **Models.** A model is a set of
  files: mostly one very large file of
  numbers (the **weights** — everything
  the model learned, written as
  numbers), plus small text files that
  say how those numbers are arranged
  and meant to be used. One model does
  one kind of job: sorting reviews into
  happy and unhappy, transcribing
  speech, drawing pictures from a
  sentence. Chapter 6 runs one.
- **Datasets.** Rows of examples: text
  with labels, questions with answers,
  pictures with captions. Datasets are
  what models learn from, and what
  honest model makers test against.
  Chapter 7 opens one and looks
  inside.
- **Spaces.** Small web apps that
  demonstrate a model in a browser:
  type a sentence, get a result, no
  install. Chapter 10 covers them in
  outline.

Models, datasets and Spaces all share
one addressing scheme. Every item has
an owner and a name, written
`owner/name`: `sshleifer/tiny-gpt2` is
a model owned by the account
`sshleifer`, named `tiny-gpt2`. That
pair of words is the item's address
everywhere — in the web page's URL, in
the download command (chapter 5), and
in code (chapters 6 to 8). Learn to
read it and the whole site becomes
legible.

## A model is files, and files are a promise

It is worth fixing one idea early,
because chapters 2, 3 and 9 all hang
from it: **when you download a model
you are accepting a bundle of other
people's work — code, data and terms —
onto your machine.** The large file of
numbers was produced by training on
some dataset, by someone, under some
**licence** (the legal terms that say
what you may do with it). Some model
files are only numbers and load
safely. Others, in older formats, can
carry runnable code (chapter 3). The
Hub page — the **model card** — is
where the maker states what the model
is, what it is for, and what the
licence allows. Reading it is not
homework before the real activity.
It is the real activity, and chapter 2
takes one apart.

This guide's own rule, stated now and
relied on throughout:

> **Read the card, check the licence,
> and download only what you are
> willing to be responsible for
> running.**

The lab behind this guide obeyed a
stricter version: no account, no
credentials, public downloads only,
and nothing larger than a few hundred
megabytes.

## Who publishes, and why so much

Anyone with an account can publish,
which is most of the Hub's character.
You will find the research labs and
the big companies (their accounts
carry a verification mark, chapter 9),
university groups, small teams, and
one person in a bedroom who fine-tuned
a model on their own poems. The same
model may appear dozens of times:
the original, copies converted to
other formats (the names often say
`-GGUF` or `-safetensors`), and
**fine-tunes** — models further
trained from someone else's starting
point. Chapter 9 is about telling
these apart, because the shelf does
not sort them for you.

## A first taste

After installing the tools
(chapter 4), this is the whole
experience in two lines — fetch a
deliberately tiny model, and look at
what arrived:

```bash
hf download sshleifer/tiny-gpt2
find ~/.cache/huggingface/hub -name 'models--sshleifer--tiny-gpt2' -type d
```

The model is a toy — a couple of
megabytes, trained to be small rather
than clever — which is exactly why
the lab used it first: every part of
the machinery (download, cache,
offline reuse) can be watched working
without waiting on a serious file.
Chapter 5 takes that command apart.

Check: the second command prints the
folder the Hub's cache made for this
model, as in the lab's transcript
`hugging-face-lab/transcripts/t02-cache-layout.txt`.
If it prints nothing, the download
did not land in the cache this guide
expects — chapter 14 starts there.

## Who it is for

The reader who has been handed a
model name — by a tutorial, a tool's
documentation, a colleague — and wants
to know what they are actually being
asked to fetch. The reader who runs
local AI and keeps meeting Hub links
inside other programs' instructions.
The reader who would like to look at
the data a model learned from, not
just the model. The common thread is
wanting to fetch with your eyes open.

## What it is not

The Hub is not a shop with a returns
desk, and a model page is not a
manufacturer's datasheet with a legal
department behind it: cards can be
incomplete, out of date, or wrong, and
chapter 13 is plain about that. It is
not the only shelf — chapter 12 maps
the neighbours, some of which hand
you the same models in friendlier
wrapping. And nothing on it is made
safe or good by being popular; the
download counts are weather, not a
verdict. Chapter 9 gives you the
checks that are actually yours to
make.
