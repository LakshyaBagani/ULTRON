"""Structural protocols for substituting fakes in place of UltronSystem."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Protocol

if TYPE_CHECKING:
    from ultron.core.config import UltronConfig
    from ultron.core.events import EventBus
    from ultron.engine._stubs import InferenceEngine
    from ultron.security.capabilities import CapabilityPolicy
    from ultron.sessions.session import SessionStore
    from ultron.tools._stubs import BaseTool
    from ultron.tools.storage._stubs import MemoryBackend
    from ultron.traces.collector import TraceCollector
    from ultron.traces.store import TraceStore


class OrchestratorDeps(Protocol):
    """Minimum surface of UltronSystem that QueryOrchestrator depends on.

    Tests can satisfy this with a lightweight class — no need to construct
    the full UltronSystem dataclass or materialize every subsystem.
    """

    config: UltronConfig
    bus: EventBus
    engine: InferenceEngine
    engine_key: str
    model: str
    agent_name: str
    tools: List[BaseTool]
    memory_backend: Optional[MemoryBackend]
    capability_policy: Optional[CapabilityPolicy]
    rate_limiter: Optional[Any]
    session_store: Optional[SessionStore]
    trace_store: Optional[TraceStore]
    trace_collector: Optional[TraceCollector]  # written by _run_agent

    # Optional attribute (getattr with default) — declared for type clarity.
    _skill_few_shot_examples: Any
