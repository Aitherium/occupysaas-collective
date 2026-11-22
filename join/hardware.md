# Hardware and model sizes

Bonsai 2 ships at four sizes. Pick the largest one that fits comfortably;
`adk bonsai-local --auto` measures the machine and makes the final call.

| RAM | model | download | good for |
|---|---|---|---|
| under 6 GB | Bonsai 2 2B | ~409 MB | a laptop or small VM; chat and light work |
| 6-11 GB | Bonsai 2 4B | ~906 MB | an ordinary desktop; the default |
| 12-23 GB | Bonsai 2 9B | ~1.9 GB | a workstation or a gaming GPU |
| 24 GB and up | Bonsai 2 27B | ~5.7 GB | a dedicated or high-VRAM box |

The embed lane needs about 1 GB and no GPU. The runner lane needs neither a
model nor a GPU -- it needs disk and the willingness to run PUBLIC
repositories' CI jobs only.

## Why the table is a recommendation, not a promise

A size that does not fit is an out-of-memory stop, and a size far below the
machine wastes it. The table errs small; `--auto` refines it with real GPU
and RAM probes. Both the model and the PrismML llama.cpp build that serves
it are downloaded once and verified before use.
