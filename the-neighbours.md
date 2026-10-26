# The Neighbours

The Hub is the biggest shelf, not the
only one, and several neighbours hand
you the same models in different
wrapping — or different models
entirely. An honest map.

## The Ollama library

**Ollama** is a program that runs
language models on your own machine
with one command, and its library is
a curated catalogue: a few hundred
models, each tested, each packaged as
the GGUF files of chapter 3, fetched
with `ollama pull` and run the same
way. Most of its catalogue started
life on the Hub — Ollama is, in large
part, a friendly front door onto Hub
files. The trade is plain: you give
up the Hub's endless choice (and its
datasets and Spaces) for a shelf
where everything on it is known to
work with the tool in your hand. This
series has an Ollama guide; many
readers will live there happily and
visit the Hub when the library does
not carry what they need.

## Civitai

**Civitai** is a community site
centred on image models — the
Stable Diffusion world especially.
Models there (often called
checkpoints) are largely the same
kinds of files, many of them
fine-tunes of Hub models, presented
with galleries of example images
instead of benchmarks. Its character
differs from the Hub in ways a reader
should go in knowing: the moderation
is looser, a meaningful share of the
catalogue is adult material, model
licences are the uploaders' own
responsibility and vary wildly, and
the same caution about `.bin`-era
formats applies with fewer scans to
lean on. For image work it is a real
and useful neighbour; it is not a
drop-in substitute for the Hub's
rigour, and chapter 9's checks matter
*more* there, not less.

## The vendors' own pages

The big model makers keep their own
shelves: OpenAI, Anthropic, Google
and others publish model pages,
documentation and prices on their own
sites. The deep difference is what is
on offer. On the Hub you download
weights and the model is *yours* to
run. On a vendor page you are usually
renting: the models stay on their
machines, you send text to an **API**
and pay per use, and no file ever
reaches your disk. Vendor pages are
where a closed model's terms, limits
and prices live, and several makers
publish their open models to the Hub
*and* rent their closed ones at home
— the same name can appear in both
worlds meaning quite different
things. Check which transaction a
page is actually offering.

## Kaggle

**Kaggle** (owned by Google) is a
data-science community built around
competitions, with its own model and
dataset shelves. Its datasets side is
deep in places the Hub is thin —
competition data, cleaned and argued
over for a decade — and its models
collection re-hosts many open models
for use in its notebook environment.
Downloading there needs an account
and its terms. Worth knowing as the
second place to look for a dataset;
for models it largely mirrors the
Hub.

## The maker's own project page

Finally, the neighbour that is easy
to forget: the model's own home — a
GitHub repository, a research page,
a paper. The card links it. That is
where the code that goes *with* the
weights usually lives, where issues
are reported and fixed, and where the
version on the Hub is revealed as a
snapshot of a moving project. When a
card and its project page disagree,
believe the project page, and note
the disagreement as a fact about the
card's upkeep.
