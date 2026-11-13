
from pathlib import Path

# 1. Çalışma ortamı
ROOT = Path(__file__).resolve().parents[3]
ALLOWED_FILES = {"README.md"}

# 2. Tool: Dosya okuma
def read_file(filename):
    if filename not in ALLOWED_FILES:
        return "ERROR: Permission denied"
    path = ROOT / filename
    if not path.is_file():
        return "ERROR: File not found"
    return path.read_text(encoding="utf-8")[:4000]

# 3. Demo model: Gerçek LLM değil!
def mock_model(history):
    if len(history) == 1:
        return {"tool": "read_file", "args": {"filename": "README.md"}}
    result = history[-1]["result"]
    return {"final": f"README içeriği:\n{result[:300]}"}

# 4. Harness: Tool çağrısı ve agentic loop
def run_agent(task):
    history = [{"role": "user", "content": task}]

    for step in range(3):
        decision = mock_model(history)

        if "final" in decision:
            return decision["final"]

        tool_name = decision["tool"]
        if tool_name != "read_file":
            return "ERROR: Unknown tool"

        result = read_file(**decision["args"])
        print(f"Step {step + 1}: {tool_name} -> {result[:60]!r}")
        history.append({"role": "tool", "result": result})

    return "Stopped: step limit reached"

print(run_agent("Bu repository'nin README dosyasını incele."))
