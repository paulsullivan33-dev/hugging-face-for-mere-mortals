# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's sentences and searches are invented for the lab.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the Hub and
   its models cannot promise: cards are their publishers'
   claims, models inherit their training data's gaps and
   skews, size is a hard wall set by the reader's machine,
   repositories move and vanish under the same name, and a
   clean scan is a floor, not a proof.
8. **The licence rule is in the text, early.** Chapter 1 and
   the README state it plainly — *read the card, check the
   licence, download only what you are willing to be
   responsible for running* — because a model licence is a
   real obligation, not metadata, and a downloaded model is
   other people's code and data: weights trained on datasets
   with terms of their own, files that older formats let
   carry runnable code, and rows of real people's words in
   every dataset. Chapters 2 and 9 return to it where the
   tooling makes crossing the line easy (gated mirrors,
   non-commercial terms, `trust_remote_code`).
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox.
Everything was installed with pip into a fresh virtual
environment (Python 3.12.3): huggingface_hub **2.3.0**,
transformers **5.20.2**, datasets **5.1.0**, torch
**2.14.1+cpu**. No Hugging Face account was created and no
credential of any kind was used; every fetch was a public,
anonymous download. All transcripts live in
`hugging-face-lab/transcripts/`; the scripts are
`hugging-face-lab/scripts/`.

Run for real, with transcripts as evidence:

- Install and versions of all four packages and the `hf`
  command (t00).
- `hf download sshleifer/tiny-gpt2`: all 9 files, about
  4.7 MB, fetched anonymously in seconds (t01).
- The cache taken apart: blobs, snapshot symlinks,
  `refs/main` naming revision
  5f91d94bd9cd7190a9f3216ff93cd1dd95f2c7be, and
  `hf cache ls` over the lab's three downloads (t02).
- Three model cards read as data via the public API —
  licences (none recorded, apache-2.0, llama3.1), complete
  file inventories with sizes (including a 32 GB gated
  repository whose metadata is public while its files are
  fenced), author, tags, gated status (t03).
- A gated download refused, live: one small file requested
  from `meta-llama/Llama-3.1-8B` anonymously, answered
  "Access denied… requires approval", exit code 1 (t08).
- A transformers pipeline run end to end: DistilBERT
  sentiment (268 MB safetensors) scoring four invented
  sentences — POSITIVE 0.9996, NEGATIVE 0.9996, a flat
  statement of fact judged POSITIVE at 0.9428, and a
  slippery sentence at 0.6328 (t04).
- The same run repeated with `HF_HUB_OFFLINE=1`, producing
  identical scores from the cache alone (t07).
- A dataset loaded and inspected: rotten_tomatoes,
  8,530 train / 1,066 validation / 1,066 test rows,
  text+label features, labels exactly balanced
  4,265/4,265 (t05).
- A tokenizer run: 30,522-entry vocabulary, special tokens,
  three texts chopped into pieces and ids — 9 tokens for
  4 words, 18 for 6 with a number in it, 11 for a line of
  code — and the [CLS]/[SEP] furniture the model actually
  receives (t06).
- Two lab traps, also real: the first dataset name the lab
  tried does not exist (the owning organisation is
  `cornell-movie-review-data`, not `cornell-movie-review`)
  — chapter 14's "repository not found" entry; and an
  interrupted first download leaving an `.incomplete`
  blob in the cache, completed by repeating the download
  — chapter 14's offline entry.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Uploading and publishing models, datasets and Spaces,
  accounts, organisations and access tokens (chapter 11):
  no account was created for this guide.
- Accepting a gated model's terms and downloading its
  files: the refusal was observed live (t08); the
  acceptance was not performed.
- Building, running and duplicating Spaces (chapter 10
  is labelled outline for this reason).
- `trust_remote_code`: never enabled in the lab, on
  purpose; chapter 9 explains the refusal as policy, not
  oversight.
- Downloading any multi-gigabyte model, and loading GGUF
  files: chapter 3's decoding is taught from real file
  inventories (t03), but no GGUF was fetched or run;
  running them is the llama.cpp and Ollama guides' ground.
- Pinning a `--revision` for a download: described in
  chapter 5; the lab downloaded at the default revision
  and recorded the hash it resolved to (t02).
- Dataset streaming: described in chapter 7; the lab
  loaded its megabyte-sized dataset whole.
- The neighbours of chapter 12 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic:
four invented sentences for the classifier, a toy model
published for testing, and a public dataset of film-review
excerpts. No example is modelled on any real person,
organisation or account, and nothing was downloaded that
was not public.
