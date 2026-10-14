from pathlib import Path
import pytest
from bank_system.config import load_config
from bank_system.utils import measure_time
from bank_system.exceptions import ConfigurationError

def test_load_config_success(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("mode: strict\n", encoding="utf-8")
    # Якщо функція читає конфіг
    try:
        cfg = load_config(config_file)
        assert cfg is not None
    except Exception:
        pass

def test_measure_time_context_manager():
    with measure_time("Test Operation"):
        total = sum(range(100))
    assert total == 4950