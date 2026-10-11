# Build Workflow — Quick Smoke

After dept-3 gate is green, run inside verified venv only:

  <venv>/Scripts/python -m pip install -r requirements.txt
  <venv>/Scripts/python -m py_compile config.py adapters.py pipeline.py bot.py
  <venv>/Scripts/python -c "from pipeline import run; print(run('test', fakes=True))"

If any step fails, return the exact exit code and stderr. Never mark as passed without running.
