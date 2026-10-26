# Sharing Your Own Work

**Outcome: you know what publishing
on the Hub involves, what a good
upload owes its readers, and where
the account line is crossed. This
chapter is documented-only from
start to finish: the lab created no
account and uploaded nothing, on
purpose, and the text does not
pretend otherwise.**

Everything before this chapter was
the reader's side of the shelf. This
one is the publisher's, described so
that the day you have something worth
sharing — a fine-tune, a cleaned
dataset, a demo — the shape of the
job is already familiar.

## What publishing takes

An account, first: the line the rest
of this guide was careful never to
need. With one, every user and every
**organisation** (a shared account for
a team) can create **repositories** —
the same `owner/name` folders you
have been downloading from — of three
kinds: model, dataset, Space. A
repository is a Git repository with
large-file handling underneath, and
it can be worked with either way:
through the web pages (create, upload
files in the browser, edit the card)
or as a programmer works: `git clone`
it, or drive it with the `hf upload`
command and the library's `upload_file`
and `create_repo` functions. Access
**tokens** — the account's keys,
created on the settings page, scoped
read-only or write — are how programs
prove who they are. A token is a
credential: stored like a password,
never pasted into code you publish,
never needed for anything public and
read-only.

## The card you owe your readers

Publishing makes you the author of
chapter 2. The reader arriving at
your page needs, from your card:

- **What it is and what it is for** —
  and what it is *not* for, in the
  out-of-scope section. Write the
  section you wished others had.
- **Where it came from** — the base
  model or source data, linked. A
  fine-tune that hides its parent is
  asking for trust it has not earned.
- **The licence, chosen deliberately.**
  Your upload's terms are yours to
  set *only within* what the things
  you built on allow: a base model's
  licence may require its terms to
  travel with derivatives, and a
  dataset's licence may forbid
  commercial use of anything trained
  on it. Publishing is where the
  licences of chapters 2 and 9 stop
  being reading comprehension and
  become your own signature.
- **How it did** — the tests you ran,
  named, with numbers you actually
  measured, and the limitations you
  already know about. Especially
  those.

The Hub provides a card template and
metadata fields (the YAML block of
chapter 2); filling them in is what
makes a model findable and its terms
machine-readable rather than implied.

## Datasets and Spaces, briefly

A dataset upload carries the same
duties plus one more: **the data
itself**. Rows in a dataset are
usually somebody's words. Publishing
them means you are asserting you had
the right to — that the source's
terms allowed it and that personal
information in it has been thought
about, not merely copied. Spaces are
published like any repository (the
code *is* the app, chapter 10), with
secrets kept in the Space's settings
rather than its files.

## Public, private, gated — your choice

Repositories can be **public** (anyone
reads, the subject of this guide),
**private** (only your account and
those you add), or **gated** (public
page, files released to accounts that
agree to your terms — the arrangement
chapter 9 met from the other side).
Private repositories are the sensible
home for experiments and drafts; a
thing does not owe the world
publication just because the button
exists. And publication is not
irrevocable — repositories can be
renamed, made private, or deleted —
but downloads already made do not
come back, which is worth one quiet
moment's thought before the first
public upload.
