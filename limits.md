# Limits

What the Hub cannot do, and what it
must not be asked to do — the chapter
the rest of the guide has been
promising.

## A shelf is not a guarantee

The Hub hosts; it does not certify.
A model page is its publisher's
document, and nothing on it was
verified by an editor: cards omit
inconvenient test results, claim
languages never tested, and go stale
as the files beneath them are quietly
updated. Popularity is not a review
process — a much-downloaded model
has been *run* often, not *checked*
often. Chapter 9's checks reduce your
risk. They do not transfer it. The
responsibility for what a model does
on your machine stays, in the end,
on your side of the download.

## The models themselves are limited

A model is a compressed shadow of its
training data, and it inherits the
data's gaps and skews as faithfully
as its skills. It can be confidently
wrong, fluent in a language it only
half knows, and biased in ways its
card does not mention because its
maker did not measure them. Small
models — the kind this guide's lab
ran — are narrower still: the
sentiment reader of chapter 6 is a
few hundred megabytes doing one small
job, and it should be believed about
exactly that job. Nothing downloaded
from any shelf becomes an authority
by being on your disk.

## Size is a wall, not a detail

The arithmetic of chapter 3 has
teeth. A model's weights must fit in
your machine's memory *alongside*
everything else the running program
needs, and the fashionable models are
tens or hundreds of gigabytes.
Quantisation lowers the wall; it
does not remove it, and the squeezed
model is a somewhat dumber model —
chapter 3 was plain that the trade
is real. A fair share of "the model
does not work" is, underneath, "the
model does not fit", and no
cleverness in this guide changes the
size of your machine.

## Licences bind in both directions

Some of what looks open is not. A
custom licence may forbid your use,
your scale, or your kind of
organisation; a non-commercial term
may reach through a model into the
app you built on it; a gated model's
terms may include acceptable-use
rules you agreed to in one click.
And the obligation runs backwards as
well as forwards: the weights you
download embed a dataset's worth of
other people's work, and "it was on
the internet" is not a term any
licence recognises. Chapter 2's
habit — read the licence first — is
the limit respected in advance;
discovering it afterwards is the
limit enforced at the worst time.

## Things move, vanish and change

A repository is its owner's folder.
Files are replaced under the same
name; models are renamed, made
private, or deleted, sometimes for
good reasons (an error, a legal
problem in the training data) and
sometimes for none. A download you
repeat next month may not be the
files you tested this month — the
tools can pin an exact **revision**
(chapter 5), and anything you come to
rely on deserves that pin. Your own
cache is the only copy whose
persistence you control.

## One company, one platform

The Hub is the largest shelf of its
kind and it is still one company's
service, run under its terms, on its
infrastructure: accounts can be
required tomorrow for things that
are free today, APIs change, and
regions can be cut off by law or
policy. The offline habits of
chapter 5 are the practical answer —
what you have cached and understood
keeps working — but the discovery
layer, the cards, the scans, the
Spaces, live on their side of the
connection.

## A scan is not a proof

The Hub's malware and pickle scans
(chapter 9) say that known-bad
patterns were not found. They cannot
say a file is good: a safetensors
file carries no code but its weights
were shaped by data you have not
seen, and a model can be exactly what
its card claims and still be the
wrong thing to trust with a real
decision. The last limit is the
oldest one in this series: the tool
fetches, loads and runs what you
point it at. Aiming it remains a
human job.
