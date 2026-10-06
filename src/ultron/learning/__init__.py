"""Learning primitive -- router policies, reward functions, learning."""

from __future__ import annotations

from ultron.learning._stubs import (
    QueryAnalyzer,
    RewardFunction,
    RouterPolicy,
    RoutingContext,
)
from ultron.learning.agents.agent_evolver import AgentConfigEvolver
from ultron.learning.learning_orchestrator import LearningOrchestrator
from ultron.learning.optimize.llm_optimizer import LLMOptimizer
from ultron.learning.optimize.optimizer import OptimizationEngine
from ultron.learning.optimize.store import OptimizationStore
from ultron.learning.routing.complexity import (
    ComplexityQueryAnalyzer,
    score_complexity,
)
from ultron.learning.routing.heuristic_reward import HeuristicRewardFunction
from ultron.learning.routing.router import (
    HeuristicRouter,
    build_routing_context,
)
from ultron.learning.training.data import TrainingDataMiner
from ultron.learning.training.lora import HAS_TORCH, LoRATrainer, LoRATrainingConfig


def ensure_registered() -> None:
    """Ensure all learning policies are registered in RouterPolicyRegistry."""
    from ultron.learning.routing.heuristic_policy import (
        ensure_registered as _reg_heuristic,
    )

    _reg_heuristic()

    from ultron.learning.routing.learned_router import (
        ensure_registered as _reg_learned,
    )

    _reg_learned()

    # Intelligence training (optional deps)
    try:
        import ultron.learning.intelligence  # noqa: F401
    except ImportError:
        pass

    # Orchestrator-specific training (optional deps)
    try:
        import ultron.learning.intelligence.orchestrator  # noqa: F401
    except ImportError:
        pass

    # Agent optimizers (optional deps)
    try:
        import ultron.learning.agents.dspy_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import ultron.learning.agents.gepa_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import ultron.learning.agents.ace_optimizer  # noqa: F401
    except ImportError:
        pass


__all__ = [
    "AgentConfigEvolver",
    "ComplexityQueryAnalyzer",
    "HAS_TORCH",
    "HeuristicRewardFunction",
    "HeuristicRouter",
    "LLMOptimizer",
    "LearningOrchestrator",
    "LoRATrainer",
    "LoRATrainingConfig",
    "OptimizationEngine",
    "OptimizationStore",
    "QueryAnalyzer",
    "RewardFunction",
    "RouterPolicy",
    "RoutingContext",
    "TrainingDataMiner",
    "build_routing_context",
    "ensure_registered",
    "score_complexity",
]
