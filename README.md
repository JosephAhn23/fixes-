# dynamo/log-report — repaired Terminal-Bench 2 (Harbor) task

Fixed Harbor task for Project Dynamo ("Fix the Broken Terminal-Bench Task").

## Verify locally

```bash
# Harbor 0.18.0, Docker running
harbor run -p log-report -a oracle     # expect reward 1.0
harbor run -p log-report --agent nop   # expect reward 0.0
```

## Defects fixed

1. `task.toml` — `artifacts` was a string pointing at `/app/out.json`; now an array `["/app/report.json"]`
2. `environment/Dockerfile` — unpinned `python:latest`; now digest-pinned `python:3.13-slim-bookworm`
3. Removed leaked `environment/solution_hint.py` from the agent image
4. Verifier now asserts real values (5 tests ↔ 5 success criteria), not merely file existence
5. `test.sh` writes `/logs/verifier/reward.txt` and `ctrf.json` (was writing to `/app/reward.txt`)
6. `instruction.md` rewritten with absolute output path, schema, and numbered criteria

Please keep this repository **private**.
