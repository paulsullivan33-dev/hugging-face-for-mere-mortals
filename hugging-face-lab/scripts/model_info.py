#!/usr/bin/env python3
"""Read public metadata for three repositories.

No files are downloaded and no account is used: model_info
asks the Hub for the card data and file list only. The third
repository is gated; the script prints whatever the Hub will
show an anonymous visitor, and says so if it refuses.
"""
from huggingface_hub import HfApi

api = HfApi()

for repo in [
    "sshleifer/tiny-gpt2",
    "distilbert-base-uncased-finetuned-sst-2-english",
    "meta-llama/Llama-3.1-8B",
]:
    print("=" * 60)
    print(repo)
    try:
        info = api.model_info(repo, files_metadata=True)
    except Exception as exc:  # gated or unreachable: report it
        print(f"  model_info refused: {type(exc).__name__}: {exc}")
        continue
    card = info.card_data or {}
    print(f"  author:      {info.author}")
    print(f"  licence tag: {card.get('license')}")
    print(f"  job tags:    {[t for t in info.tags if ':' not in t][:6]}")
    print(f"  gated:       {info.gated}")
    print(f"  downloads:   {info.downloads}")
    total = 0
    print("  files:")
    for sibling in info.siblings:
        size = sibling.size or 0
        total += size
        print(f"    {sibling.rfilename:<45} {size:>12,} bytes")
    print(f"  total size:  {total:,} bytes")
