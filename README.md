# tiny-chess-ci

Trial runner for the tiny-chess-01 make.fun entry (4KB Python chess engine).
Runs practice trials on GitHub Actions (free for public repos, 2-core runners).

## How to run a trial

Actions -> "Chess trial" -> Run workflow -> pick bot dir (v9r2) and trial number (0-2).
Results (result.txt, bot.log, env.log) are uploaded as an artifact.

## Layout

- `bots/<name>/main.py` - bot payload (<=4096 bytes, self-extracting).
- `run-trial-ci.sh` - trial runner (env server + bot + scorer).
- `.github/workflows/trial.yml` - the workflow. Downloads the make.fun kit at runtime.

## Bots

- `v9r2` - PVS + history, no taper, ND=150000, 4077 bytes. Mean 1377 Elo (t0 1290, t1 1464).
- `v4` (submitted to make.fun) - mean 1371 Elo, leaderboard 1326.
