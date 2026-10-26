# Datasets, Loading and Looking

**Outcome: you can load a published
dataset, say what is in it — rows,
columns, splits, labels — and judge
whether it is the size you thought
it was before fetching a bigger one.**

The datasets shelf is the quiet half
of the Hub, and the half that makes
the other half honest: models are
trained and scored on datasets, and
a model's card (chapter 2) names the
ones it used. The **datasets**
library is the shelf's reading room.

## Loading one

The lab's script
(`hugging-face-lab/scripts/look_at_dataset.py`)
loads a genuinely small one:

```python
from datasets import load_dataset

ds = load_dataset("cornell-movie-review-data/rotten_tomatoes")
```

One line, and behind it the familiar
machinery: the dataset's files
arrive through the same cache as
chapter 5 (datasets keep their own
corner of it), in an efficient
column format, ready to read. This
one is about a megabyte: short
excerpts from film reviews, each
labelled positive or negative — the
same *kind* of material chapter 6's
model was fine-tuned on, which is
why the lab chose it. Transcript t05
keeps the run.

## What you are holding

`load_dataset` returns a bundle of
**splits** — named slices with
separate jobs:

- **train** — the rows a model may
  learn from.
- **validation** — rows held back to
  check learning as it goes.
- **test** — rows held back for the
  final, honest score.

The split discipline is the shelf's
core etiquette: testing a model on
rows it trained on proves nothing,
and a benchmark result (chapter 2)
is only meaningful because the test
split was never in the training.
Each split is a table. Its
**features** — the column names and
types, printed in the transcript —
are the dataset's schema: here,
`text` (a string) and `label` (one
of two named classes). Reading rows
is deliberately plain: index one
out, or `select` a few, and they
arrive as ordinary dictionaries.

Check: the script prints the first
rows, the first validation row, and
the label counts. Answer from the
transcript: how many rows in train,
and are the two labels balanced?
Imbalance is the first thing to know
about any dataset, because a model
trained on nine-to-one data has
learned nine-to-one opinions.

## Looking before you load

Everything chapter 2 taught about
model cards applies here with the
names changed: a **dataset card**
states where the rows came from, who
collected them, what licence covers
them, and what personal information
might be inside. Size, too: dataset
pages list their files, and the
famous ones are not megabytes but
hundreds of gigabytes. Two defences:
read the card's size before the
`load_dataset` line, and remember
that most datasets can be *streamed*
— read row by row without storing —
when all you need is a look. The lab
loaded its megabyte whole and says
so; streaming is described here from
the documentation, not run.

And one sentence of chapter 9's,
repeated where it belongs: rows in a
dataset are usually real people's
words, gathered under some terms.
The dataset card is where those
terms live.
