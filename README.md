# Ultron

**Personal AI, on your own devices.**

Ultron is a framework for building local-first personal AI agents. It runs language
models directly on your hardware by default and only reaches out to the cloud when a
task genuinely needs it — so your "personal" AI stays personal.

## Why Ultron

Most personal AI assistants route everything through someone else's servers. Local
models have become good enough to handle the large majority of everyday chat and
reasoning tasks, and consumer hardware keeps getting faster. What has been missing is
the software stack that makes local-first personal AI practical to build and run.

Ultron is that stack. It is built around three ideas:

- **Shared primitives** for building on-device agents — models, tools, skills,
  memory, sessions, and scheduling.
- **Cost-aware evaluations** that treat energy, latency, and dollar cost as
  first-class constraints alongside accuracy.
- **A learning loop** that improves agent behavior from your own local trace data.

## Features

- **Local-first inference** — run models through Ollama and other local engines, with
  an optional cloud fallback you control.
- **Built-in agents** across on-demand, scheduled, and continuous execution modes
  (chat, deep research, morning digest, long-horizon monitoring, code execution, and
  more).
- **Skills** — reusable capabilities that teach agents how to use tools and reason
  better; agents discover them from a catalog and invoke them on demand.
- **Connectors** for your own data sources (email, calendar, files, and others).
- **Desktop GUI** (Tauri + React) alongside a full command-line interface.
- **A native Rust core** for performance-sensitive work, exposed to Python.

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) for environment and dependency management
- [Ollama](https://ollama.com/) (or another supported engine) for local inference
- Node.js 22+ (only for the desktop GUI)
- Rust toolchain (only to build the native extension from source)

## Installation

```bash
# Clone and enter the project
cd Ultron

# Install dependencies into a virtual environment
uv sync

# (Optional) install developer extras
uv sync --extra dev
```

## Quick Start

```bash
uv run ultron                         # start chatting
uv run ultron gui                     # launch the graphical interface
uv run ultron init --preset <name>    # start from a preset configuration
uv run ultron doctor                  # check your setup
```

Prefer a shorter command? Activate the environment first and drop the `uv run` prefix:

```bash
source .venv/bin/activate
ultron
```

### Presets

| Preset | What it does |
|---|---|
| `chat-simple` | Lightweight conversation, no tools |
| `morning-digest` | Spoken daily briefing from email, calendar, and news |
| `deep-research` | Multi-hop research across indexed docs with citations |
| `code-assistant` | Agent with code execution, file I/O, and shell access |
| `scheduled-monitor` | Stateful agent that runs on a schedule with memory |

### Skills

```bash
# Use a skill with any agent
uv run ultron ask "Use the code-explainer skill to explain: for i in range(5): print(i)"

# Optimize skills from your trace history
uv run ultron optimize skills

# Benchmark their impact
uv run ultron bench skills
```

## Development

```bash
uv sync --extra dev
uv run pre-commit install
uv run pytest tests/ -v
```

The project layout:

- `src/ultron/` — the Python package (CLI, agents, server, evals, skills)
- `rust/` — the native Rust workspace and PyO3 extension
- `frontend/` — the Tauri + React desktop GUI
- `configs/` — default configuration and presets
- `docs/` — documentation sources
- `tests/` — the test suite

## License

[Apache 2.0](LICENSE)
