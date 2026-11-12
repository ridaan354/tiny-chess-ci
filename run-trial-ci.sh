#!/bin/bash
# Run one practice trial (0,1,2) against a bot dir holding main.py, then score it.
# CI version of run-trial.sh: kit is at ./kit (downloaded by the workflow).
# Usage: run-trial-ci.sh <trial> <bot-dir> <tag>
set -u
TRIAL=${1:?trial}
BOT=${2:?bot-dir}
TAG=${3:-t$TRIAL}
KIT=./kit
BASE=./trials/$TAG
mkdir -p "$BASE"
STATE="$BASE/state"
rm -rf "$STATE"; mkdir -p "$STATE"
export MAKEFUN_ENV_DATA_DIR="$KIT/practice/trial-$TRIAL/input/env"
export MAKEFUN_STATE_DIR="$STATE"
export MAKEFUN_ENV_PORT=18080
node "$KIT/program/env/server.mjs" > "$BASE/env.log" 2>&1 &
ENV_PID=$!
for i in $(seq 1 50); do grep -q '"schema"' "$STATE/ready" 2>/dev/null && break; sleep 0.2; done
export MAKEFUN_ENV_URL="http://127.0.0.1:18080"
export MAKEFUN_PROMPT_FILE="$KIT/practice/trial-$TRIAL/input/prompt.txt"
START=$(date +%s)
python3 -P -s "$BOT/main.py" > "$BASE/bot.log" 2>&1
BOT_RC=$?
END=$(date +%s)
kill -TERM $ENV_PID 2>/dev/null
wait $ENV_PID 2>/dev/null
echo "bot rc=$BOT_RC wall=$((END-START))s" | tee "$BASE/result.txt"
export MAKEFUN_OUTPUT_DIR="$STATE/export"
export MAKEFUN_REFERENCE_DIR="$KIT/practice/trial-$TRIAL/reference"
export MAKEFUN_SCORES_DIR="$BASE/scores"
node "$KIT/program/scorer/score.mjs" 2>&1 | tee -a "$BASE/result.txt"
echo "--- bot log tail ---"; tail -20 "$BASE/bot.log"
