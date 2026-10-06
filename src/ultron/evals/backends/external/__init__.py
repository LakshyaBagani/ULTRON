"""External-framework subprocess backends (Hermes Agent, OpenClaw)."""

from ultron.evals.backends.external.hermes_agent import HermesBackend
from ultron.evals.backends.external.openclaw import OpenClawBackend

__all__ = ["HermesBackend", "OpenClawBackend"]
