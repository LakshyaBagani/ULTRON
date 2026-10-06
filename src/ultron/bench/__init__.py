"""Benchmarking framework for Ultron inference engines."""

from __future__ import annotations

from ultron.bench._stubs import BaseBenchmark, BenchmarkResult, BenchmarkSuite
from ultron.core.registry import BenchmarkRegistry


def ensure_registered() -> None:
    """Ensure all benchmark implementations are registered."""
    from ultron.bench.energy import ensure_registered as _reg_energy
    from ultron.bench.latency import ensure_registered as _reg_latency
    from ultron.bench.throughput import ensure_registered as _reg_throughput

    _reg_latency()
    _reg_throughput()
    _reg_energy()


# Trigger registration on import
ensure_registered()

__all__ = [
    "BaseBenchmark",
    "BenchmarkRegistry",
    "BenchmarkResult",
    "BenchmarkSuite",
    "ensure_registered",
]
