# Publishing a dataset on Hugging Face under the W2FPL

1. Create a dataset repo on huggingface.co (for example `snvrk/snvrkotics-data`).
2. Upload `dump.ndjson` from https://data.snvrkotics.com/dump.ndjson.
3. Use `README.md` in this folder as the dataset card. The front matter sets
   `license: other` with `license_name: w2fpl-1.0` and `license_link`, which is how
   Hugging Face takes a license that isn't on its list.
4. Set `size_categories` to the real row count (n<1K, 1K<n<10K, 10K<n<100K, ...).
5. Do the same for dripgraph (https://dripgraph.com/dump.ndjson). Leave out any
   photos: the W2FPL covers dripgraph's data, not its images.
