# The hf Command Line

**Outcome: you can fetch exactly the
files you chose, find them again on
your own disk, and keep working when
the network goes away.**

## Downloading, whole and in part

The one command this guide leans on:

```bash
hf download sshleifer/tiny-gpt2
```

Name the repository, and the whole of
its current version arrives — for the
lab's toy model, nine files in a few
seconds (transcript
`hugging-face-lab/transcripts/t01-cli-download.txt`).
Notice what the command printed at the
end: not a folder in your current
directory, but a path deep inside the
**cache**. Downloads on the Hub go to
the cache first; tools then read from
there. More control, when you want it:

- **Named files only.** Add filenames
  to fetch just those:
  `hf download owner/model config.json`.
  On a repository whose weights come
  in five flavours (chapter 3), this
  is how a person downloads *one*
  GGUF and not the whole shelf —
  often the difference between 4 GB
  and 40.
- **Patterns.** `--include '*.json'`
  fetches every file matching a
  pattern; `--exclude` skips. Between
  the two, "the small text files, not
  the weights" is one command.
- **A particular version.**
  `--revision` takes a **revision** —
  the commit hash that names one exact
  state of the repository. Pinning a
  revision is how a download becomes
  repeatable (chapter 13 explains why
  that matters), and the Files tab on
  the web page shows the current one.
- **A dataset instead.** `--repo-type
  dataset` before the name; Spaces
  take `--repo-type space`. Same
  command, other shelves.

## The cache, taken apart

Everything fetched lands under
`~/.cache/huggingface/hub` (a
different home can be set with the
`HF_HOME` environment variable). One
folder per repository, named
`models--owner--name`, and inside it
a structure worth understanding
once, because every "where did it
go" question in chapter 14 is
answered here. The lab's dissection
is transcript t02
(`hugging-face-lab/transcripts/t02-cache-layout.txt`):

- **`blobs/`** — the actual bytes,
  one file per downloaded file, named
  by a hash of its contents. Identical
  files shared between models or
  versions are stored exactly once.
- **`snapshots/<revision>/`** — one
  folder per downloaded version, whose
  entries are **symbolic links** into
  `blobs/`, wearing the real
  filenames. This is the folder tools
  actually open, and the path the
  download command printed.
- **`refs/main`** — a tiny file
  containing the revision hash that
  `main` currently means for this
  repository: the cache's own answer
  to "which version is 'latest' here".

Two habits follow. First, **never
edit inside the cache**: it is a
store with its own bookkeeping, and
a file changed there corrupts every
snapshot that links to it. Copy out
what you want to alter. Second,
**the cache is yours to reclaim**:
`hf cache ls` lists what is held and
what it weighs, and `hf cache rm`
removes repositories by name.

## Working offline

Fetch first, then cut the cord: with
the environment variable
`HF_HUB_OFFLINE=1` set, the tools use
only the cache and say so, instead of
checking the Hub for fresher files.
The lab ran chapter 6's model that
way as its last experiment
(transcript t07): the run is
indistinguishable from the online
one, because by then everything it
needed was already home. Offline
mode is also a fine lie detector for
chapter 14: if a program claims to
work offline and fails this way, the
thing it needs was never actually in
your cache.

Check: download the toy model, then
run any later chapter's command with
`HF_HUB_OFFLINE=1` in front of it.
If it works, you understand the
cache. If it complains, chapter 14's
offline entry names the two usual
reasons.
