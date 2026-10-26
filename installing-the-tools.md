# Installing the Tools

**Outcome: the `hf` command answers,
and Python can import the libraries
the rest of the guide uses.**

Two pieces of software do everything
in this guide: the **`hf` command
line** (fetching files and managing
the cache, chapter 5) and the
**transformers** library (running
models from Python, chapters 6 to 8).
Both arrive by **pip**, Python's
installer, into a **virtual
environment** — a private folder of
Python packages that leaves the rest
of the machine alone. The lab's
versions are in transcript
`hugging-face-lab/transcripts/t00-versions.txt`:
huggingface_hub 2.3.0, transformers
5.20.2, datasets 5.1.0, on Python
3.12. Yours will differ in the small
digits; the commands will not.

```bash
python3 -m venv ~/hf-venv
~/hf-venv/bin/pip install huggingface_hub transformers datasets torch
~/hf-venv/bin/hf version
```

Three honest warnings about that
second line:

- **It is a large download.** The
  transformers library rides on
  **PyTorch** (`torch`), the engine
  that does the arithmetic, and the
  standard package is hundreds of
  megabytes even before any model
  arrives. On a metered connection,
  install at a generous moment.
- **Ask for the CPU build if that is
  your machine.** The lab's machine
  has no graphics card for this work,
  and installed PyTorch's CPU-only
  build (its version prints as
  `2.14.1+cpu`), which is far smaller
  than the build that bundles
  graphics-card machinery you would
  never use. PyTorch's site keeps a
  selector that produces the exact
  install line for your machine;
  using it is the difference between
  a heavy install and a silly one.
- **`hf` needs no account for this
  guide.** The installer may hint
  that signing in raises rate limits.
  For public downloads at this
  guide's scale, anonymous fetching
  is fine, and chapter 1's rule was
  deliberate: no credentials, so no
  credentials can leak, expire, or
  confuse a refusal (chapter 14 has
  the story of the stale token).

Check: `hf version` prints its
version, and this prints nothing at
all if a library is missing:

```bash
~/hf-venv/bin/python -c "import huggingface_hub, transformers, datasets, torch; print('all present')"
```

The lab's printout said `all
present`, and yours should too
before chapter 5 asks the new tools
to fetch something.
