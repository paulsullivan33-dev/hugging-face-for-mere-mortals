# Judging What to Trust

**Outcome: you have a short,
repeatable set of checks to run on
any model before it earns a place on
your machine.**

Chapter 1's rule said: download only
what you are willing to be
responsible for running. This chapter
is how you decide. None of the checks
is conclusive alone; together they
separate the maintained, honest
shelves from the rest quickly.

## Who is offering it

Start with the owner half of the
name. Organisations of standing —
research labs, universities, the
companies that trained the famous
models — publish under accounts the
Hub marks as **verified**, with
their name, site and history
attached. An individual publisher is
not thereby suspect, but the evidence
shifts: with a known organisation,
their reputation is hostage to the
upload's quality. Either way, look at
the account: how old, how many
models, whether *this* one is their
kind of work. The classic bad shelf
is a famous model name under a
stranger's account, uploaded last
week, with the card copied and the
files changed. When the original
exists, fetch the original.

## The card as evidence

Chapter 2's reading order doubles as
an audit. A card that names its
training data, its tests, its
limitations, and a licence you can
point at is a maker showing their
working. Vague cards — no data named,
no results, "best model!!" — are not
proof of a bad model, but they move
the burden of proof onto you, and
the files below get read harder.

## The files, and the scans

Open the Files tab (chapter 2) and
read it like an inventory:

- **Formats.** safetensors offered
  alongside (or instead of) pickle
  `.bin` files is the modern, safe
  pattern. A repository whose only
  weights are `.bin` is either old or
  careless (chapter 3 explains the
  pickle risk in full).
- **Scan results.** The Hub scans
  uploads — for malware signatures
  and for dangerous pickle content —
  and shows the outcome on the files
  page. A clean scan is a floor, not
  a ceiling (chapter 13), but a
  flagged file is a closed door: do
  not load it to see what happens.
- **Stray code.** Files ending `.py`
  mean the model wants to run its
  publisher's code on load. The
  loading tools refuse unless told
  `trust_remote_code=True` — a switch
  named with unusual honesty. Almost
  no model needs it. Treat the request
  the way you would treat a download
  page that asks you to disable your
  antivirus to proceed: the legitimate
  cases exist, and you are not obliged
  to be one of them. This guide never
  flips that switch.

## Gated models: the fence with a form

Some models are **gated**: the card
is public, the files sit behind a
form — you need an account, you give
your name, you click agreement to the
maker's terms, sometimes a human or
a process approves. The lab met this
from outside, on purpose. Reading a
gated model's public metadata with
no account shows a surprising amount
— the maker's name, the licence, the
complete file list with sizes —
because what is fenced is the
*downloading*, not the describing
(`hugging-face-lab/transcripts/t03-model-info.txt`).
The fence itself is in transcript
t08: asked for one small file from
a gated repository, the tools answer
*access denied, requires approval*
and stop. That is exactly the
arrangement working as intended.
Gating is not a mark against a model;
it is a maker exercising a licence
that was never the open kind. What
you may not do is treat the fence as
a puzzle: mirrors of gated files
under other names exist, and taking
them means taking the model *without*
the agreement — the one part of the
deal that was actually for you.

## Numbers that only look like evidence

Downloads and likes measure attention.
A model is downloaded heavily because
a popular tool defaults to it, because
a tutorial named it in 2023, because a
botnet of mirrors copied it last
night. Use the numbers to find the
canonical copy (the most-downloaded
`owner/name` for a famous model is
usually the real shelf), never to
conclude the model is good, current,
or safe.

## The community tab, briefly

Every repository has a discussion
area. Skim it before downloading
anything large: unanswered "this file
is corrupted" reports, a publisher
who has vanished mid-argument, users
noting the card's claims don't match
the files — all cheaper to learn
there than from your own error
messages. A quiet tab on an old,
finished model means nothing either
way.

Check: take the last model someone
recommended to you and run it through
this chapter — verified owner or the
original found, card read, files
inventoried, formats safe, scans
clean, no code requested. Five
minutes. Whatever survives that is
a reasonable download; whatever does
not was never really recommended,
only mentioned.
