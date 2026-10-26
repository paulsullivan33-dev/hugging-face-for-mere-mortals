# Troubleshooting

Symptom first, cause second, in the
order the lab and the documentation
suggest you check them.

## "Download worked before; now it asks me to log in"

*The model was public yesterday. The
error is a 401 or 403.*

1. **The model went gated, or always
   was.** Owners change the fence
   (chapter 9). Check the model's
   page: a banner asking you to agree
   to terms means an account and a
   clicked agreement are now part of
   the price.
2. **A stale token is lying around.**
   If you (or a tool) once saved a
   login token that has since expired
   or been revoked, the tools may send
   the bad token and be refused where
   an anonymous request would sail
   through. Logging out
   (`hf auth logout`) restores the
   anonymous lane for public files.

## "Repository not found" for a model that exists

1. **The name is misspelled — often by
   the autofill of your own memory.**
   Owner/name pairs are exact,
   including dashes and case patterns;
   copy the pair from the page's URL.
2. **It is private or gated**, and
   from outside, the Hub answers
   "not found" for both — deliberately,
   so existence itself is not leaked.

## Offline mode says the model is not in the cache

*You set offline mode and the tool
insists the model was never
downloaded.*

1. **It wasn't — not all of it.** A
   download interrupted halfway leaves
   a partial snapshot. Offline mode
   refuses leftovers rather than
   guessing. Go online once, repeat
   the download until it completes,
   then go offline.
2. **There are two caches.** Tools
   honour the `HF_HOME` environment
   variable; if one shell sets it and
   another doesn't, each sees a
   different, honest cache. Settle
   which folder each command is
   reading before downloading
   anything twice.

## The first run of a pipeline downloads for a long time

*You wrote three lines (chapter 6)
and the machine has been fetching
ever since.*

1. **The task's default model is not
   small.** A pipeline with no model
   named picks a default, and some
   defaults are gigabytes. Name the
   model you actually read the card
   of. That was the whole point of
   chapters 2 and 6 being adjacent.
2. **It is also fetching the tokenizer
   and configuration — once.** Later
   runs read the cache (chapter 5)
   and start in seconds. The long
   first run is the tuition; the lab's
   transcript t04 shows it in full.

## "Out of memory" loading a model that "should fit"

1. **The file fitting is not the model
   fitting.** Running needs the weights
   *plus* working room, and the loading
   program may briefly hold two copies.
   Chapter 13's wall is measured in
   RAM free, not disk space.
2. **Take the smaller quantisation.**
   On a GGUF shelf, stepping from
   Q8_0 to Q5_K_M to Q4_K_M (chapter
   3) is the intended way down the
   ladder. Expect each step to cost a
   little sharpness, not to halve it.

## A `.bin` file triggers a pickle warning

*The scanner or the loading library
objects to an old-format weights
file.*

1. **Believe it.** The warning is the
   system working (chapter 3). Look
   for the safetensors conversion —
   many repositories carry both, and
   the Hub often generates a
   safetensors copy on the model's
   page. If none exists, the model's
   age and upkeep just became your
   decision, not your accident.

## Tokenizer complaints: files missing or vocab mismatch

1. **The tokenizer is not in the same
   repository.** Some collections put
   the model and its tokenizer in
   different folders. Both halves come
   from the same maker's page; a
   tokenizer borrowed from *another*
   model (chapter 8) produces fluent
   garbage with no error at all — the
   worst failure shape in this book.
   If there is no error and the output
   is nonsense, suspect this first.

## It worked online; offline it is slow to fail, then fails

1. **Something *else* was not cached.**
   A program may reach for a config or
   a second model's files at start-up.
   Run it once online and watch what
   it fetches (the cache directory's
   new folders are the list), then try
   offline again with the set
   complete.
