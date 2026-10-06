"""Smoke test that the tmp_ultron_home fixture works."""

from __future__ import annotations

from pathlib import Path

from ultron.core import config as config_mod


def test_fixture_redirects_default_config_dir(tmp_ultron_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_DIR == tmp_ultron_home
    assert tmp_ultron_home.exists()
    assert (tmp_ultron_home / ".state").exists()
    assert (tmp_ultron_home / ".state" / "models").exists()


def test_fixture_redirects_config_path(tmp_ultron_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_PATH == tmp_ultron_home / "config.toml"
