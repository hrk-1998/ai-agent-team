# Build Workflow — Quick Smoke

After dept-3 gate is green, run inside the verified runtime only:

Python stack:

  <venv>/Scripts/python -m pip install -r requirements.txt
  <venv>/Scripts/python -m py_compile config.py adapters.py pipeline.py bot.py
  <venv>/Scripts/python -c "from pipeline import run; print(run('test', fakes=True))"

Node stack:

  npm ci
  npm run build

RUN & SHOW (app-builder smoke): after a passing build, boot the dev server,
health-check the URL until HTTP 200, and record the URL:

  npm run dev &        # or: <venv>/Scripts/python -m serve
  curl -s -o /dev/null -w "%{http_code}" http://localhost:<port>/

If any step fails, return the exact exit code and stderr. Never mark as passed without running.
RUN_BLOCKED (server never healthy after one restart) = smoke FAIL with log tail.
