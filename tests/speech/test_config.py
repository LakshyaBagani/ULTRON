"""Tests for speech configuration."""

from ultron.core.config import UltronConfig, SpeechConfig


def test_speech_config_defaults():
    cfg = SpeechConfig()
    assert cfg.backend == "auto"
    assert cfg.model == "base"
    assert cfg.language == ""
    assert cfg.device == "auto"
    assert cfg.compute_type == "float16"


def test_ultron_config_has_speech():
    cfg = UltronConfig()
    assert hasattr(cfg, "speech")
    assert isinstance(cfg.speech, SpeechConfig)
    assert cfg.speech.backend == "auto"


def test_ultron_system_has_speech_backend():
    """UltronSystem has a speech_backend attribute."""
    from ultron.system import UltronSystem

    assert "speech_backend" in UltronSystem.__dataclass_fields__
