# Tokenizers

**Outcome: you can explain what a
tokenizer does, run one, and read its
output — and you will never again
assume a model counts words the way
you do.**

Before a model can read your sentence,
something must turn the sentence into
numbers, because numbers are all the
model ever sees. That something is
the **tokenizer**, and the numbers it
produces are **tokens**.

## What a token is

A **token** is a piece of text from
the tokenizer's dictionary — sometimes
a whole word, often a fragment:
common words get their own entries,
rare words are assembled from parts.
Feed the sentence *"Tokenizers are
unreasonably effective"* to the
tokenizer the lab used (it belongs to
the sentiment model of chapter 6) and
it comes back as a list of pieces,
then as the list of numbers those
pieces are numbered with in the
dictionary — the lab's run is
`hugging-face-lab/transcripts/t06-tokenizer.txt`.
Two properties visible right in that
transcript are worth naming:

- **It lowercases.** This tokenizer
  belongs to an *uncased* model: it
  folds `The` and `the` into one
  entry. Capitalisation is information
  the model never receives. Other
  models' tokenizers are *cased* and
  keep the distinction. Neither is
  better; each model was trained with
  its own, and they are not swappable.
- **It adds furniture.** The number
  list begins and ends with entries
  that are not in your sentence: this
  family's special tokens mark where a
  sequence starts and where segments
  separate. Every tokenizer has a few
  such marks — padding, unknown-word,
  end-of-text — and they count toward
  the totals below.

The dictionary itself (the **vocab**)
is a file in the model's repository —
about thirty thousand entries for the
lab's model, hundreds of thousands
for some modern ones. Chapter 3 said
a model and its tokenizer are a
matched pair; this is why. The
numbers only mean what *this*
dictionary says they mean.

## Why anyone should care

Three practical consequences follow,
and all three bite in real use:

**Length is counted in tokens, not
words.** Every model has a maximum
sequence length — its context — and
it is measured in tokens. The rough
rule for English is a token per
three-quarters of a word, but code,
other languages, and text full of
rare words or numbers all tokenize
hungrier. When a tool says a document
was "too long", this arithmetic is
what happened.

**Cost and speed follow tokens.**
Hosted models bill by the token, and
local ones spend time per token. The
tokenizer's count (there is a number
in the transcript) is the honest
predictor of both, not the word
count.

**Odd behaviour is often a token in
disguise.** Models famously stumble
over counting letters in a word, or
reversing a string, partly because
they never see letters — they see
whole pieces. Knowing the pieces
exist turns "the model is stupid"
into the more useful "the model
literally cannot see that".

Check: run the lab's script
(`hugging-face-lab/scripts/tokenizer_play.py`)
on a sentence of your own, then on a
line of code or a long number, and
watch how differently the two are
chopped.
