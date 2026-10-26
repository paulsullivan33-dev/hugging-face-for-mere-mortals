# Reading a Model Card

**Outcome: given any model page, you
can find its licence, its biggest
file, what its maker says it is for,
and what they say it should not be
used for — before anything is
downloaded.**

A **model card** is the page a model
lives on: part shop window, part
manual, part legal notice. It is
written by whoever published the
model, in a format the Hub encourages
but does not enforce. Cards range
from a careful document with test
results to a single line and a
shrug — and that range is itself
information (chapter 9 uses it).

## The parts, top to bottom

**The name and the tags.** At the top:
`owner/name`, then small tags the
publisher chose — the job the model
does (`text-classification`,
`text-generation`, `image-to-image`),
the library it works with
(`transformers`, `gguf`), the
languages it claims, and its size
class (`0.1B`, `7B` — billions of
**parameters**, the numbers in the
weights file). The size tag is your
first feasibility check: chapter 3
turns it into gigabytes.

**The licence tag.** Near the tags
sits the single most consequential
word on the page: the **licence**.
Common sights, in plain terms:

- `apache-2.0` and `mit` — the
  permissive classics from ordinary
  software. Use it, build on it, sell
  things made with it, keep the notice.
- `cc-by-4.0` and family — attribution
  required: credit the maker, say what
  you changed. The `-nc-` variants add
  *non-commercial*: no selling.
- `openrail` and relatives — permissive
  with use restrictions attached:
  certain harmful uses are forbidden
  by the licence itself.
- A model's own name — `llama3.1` and
  similar. Some large models ship
  under a custom **community licence**
  written by their maker: often free
  to use, with conditions (accepting
  the terms, limits at very large
  scale, naming rules). It is not the
  same as the open licences above, and
  the difference matters if you build
  anything public on it.
- `other`, or nothing at all — the
  terms are in the card text if
  anywhere, or nowhere. Nothing at all
  does not mean "no rules"; in most
  legal systems it means the default
  rules, which give you very little.

Treat the licence as part of the
download, because it is: a contract
you accept by using the model, not
decoration on the page. If the
licence forbids what you were
planning, the model is not for you,
however well it would work.

**The card text.** Below the tags, the
maker's own document. The sections a
complete card carries, and what to
look for in each:

- *What it is* — the job, the starting
  point it was trained from, who made
  it.
- *How to use it* — example code,
  usually the **pipeline** call of
  chapter 6.
- *Intended use* and *out of scope* —
  the maker's own statement of what
  the model is for and what it is not
  for. A maker who writes this section
  carefully is telling you they thought
  about misuse; a missing section is
  also a message.
- *Training data* — which datasets,
  named so you can go and read *their*
  cards on the datasets shelf. A model
  is downstream of its data, always.
- *Results* — scores on named tests
  (**benchmarks**). Comparable only
  when the test and conditions match
  another model's — a number without
  its test named is advertising.
- *Limitations and bias* — where the
  maker knows it fails or skews. The
  most honest section of any card, and
  the one most often skipped by
  readers in a hurry.

**Files and versions.** A tab on every
model page, and the one chapter 3
needs you to be comfortable in. It
lists every file in the **repository**
(the model's folder on the Hub): the
weights in whatever formats the maker
supplied, the small text files, and
each file's size. Read it *before*
downloading. It answers: how many
gigabytes is this really, is there a
small format variant, and is there
anything here that is not a model at
all (chapter 9 cares).

**The metadata block.** At the very
top of the card's source sits a block
of **YAML** — machine-readable facts
(licence, job, languages, datasets
used) that the Hub reads to build the
tags and search results. You rarely
need it as a reader; it matters in
chapter 11, when the card is yours.

## A worked read, without downloading

The lab read several cards through
the Hub's own machinery rather than
a browser, and the transcript
(`hugging-face-lab/transcripts/t03-model-info.txt`)
shows the same facts arriving as
data: the licence tag, the file list
with sizes, the author, and one more
field the web page shows as a banner —
whether the model is **gated**, asking
you to agree to terms before files
are released (chapter 9). Everything
in that transcript came from public
metadata; no file was downloaded and
no account was used.

Check: pick a model you have heard of
and answer, from its card alone —
who made it, what is the licence,
what is the largest file, and what
does the maker say it is not for. If
you cannot answer all four, you have
learned the most important fact about
that card.
