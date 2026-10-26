# Spaces

**Outcome: you can explain what a
Space is, what visiting one actually
does, and what it costs and risks —
in outline. This chapter is
documented-only: the lab used no
account and deployed nothing, so it
describes Spaces from the project's
documentation and the public pages
themselves, and says so.**

A **Space** is a small web app
attached to a model (or a dataset, or
neither): a page with boxes to type
in and a result that appears. Spaces
are the Hub's showroom floor. A model
whose card leaves you cold often has
a linked Space where thirty seconds
of typing tells you more than the
benchmarks did.

## What visiting one does

You open the page, the app runs on
**Hugging Face's machines** — not
yours — and your input is sent there,
processed, and the answer returned.
Three consequences worth holding:

- **Nothing is installed and no file
  is downloaded.** A Space is a way to
  *test* a model before committing
  gigabytes to it. Used that way, it
  is the cheapest tool in this whole
  guide.
- **Your input leaves your machine.**
  Whatever you type or upload goes to
  their servers and, depending on the
  Space's own setup, may be logged by
  its owner. Treat a Space like a
  stranger's website, because that is
  what it is: never paste anything
  private into one.
- **It demonstrates; it does not
  promise.** A Space runs the model
  its owner chose, with their settings,
  on their hardware tier. The same
  model on your machine, differently
  set up, may behave better or worse.

## The shapes they come in

Most Spaces are built with **Gradio**
— a Python library from Hugging Face
that turns a function into a web form
— or **Streamlit**, its independent
cousin, and the page usually says
which. Some are plain static pages,
and some are full **Docker** apps, a
freedom that lets a Space be almost
anything, including barely a model
demo at all. The Space's own Files
tab shows its source, which is the
honest way to answer "what does this
one do with my input": read the
`app.py`.

## Hardware, queues and sleep

Spaces run on tiers. Free Spaces run
on modest shared CPUs, may queue at
busy times, and **sleep** when idle —
the first visitor after a nap waits
while the machine wakes and the model
loads. Owners can pay for GPU tiers
and persistence. A slow or sleeping
Space is a fact about its tier, not
about the model it demonstrates; do
not grade a model by its free
showroom's patience.

## Making and copying Spaces

Building a Space, and **duplicating**
one (the one-click copy that lets you
run someone else's demo on your own
account's hardware — the standard way
to get a private or faster copy), both
need an account, and a duplicated
Space may need the original's secrets
or paid tier to work at all. That is
account territory, so it belongs to
chapter 11's documented-only ground:
described here in outline, not
performed, and not needed for
anything else in this guide.
