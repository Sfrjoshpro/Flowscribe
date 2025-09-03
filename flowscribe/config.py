"""
Config loader for flowscribe (YAML + env overrides)
"""
import os
import yaml

def load_config(path: str = ".autodev/ra.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    # Apply environment variable overrides
    config["enabled"] = _env_bool("RA_ENABLED", config.get("enabled", True))
    if "RA_PROFILE" in os.environ:
        config["profile"] = os.environ["RA_PROFILE"]
    if "RA_INCLUDE" in os.environ:
        config.setdefault("filters", {})["include_flows"] = os.environ["RA_INCLUDE"].split(",")
    if "RA_EXCLUDE" in os.environ:
        config.setdefault("filters", {})["exclude_flows"] = os.environ["RA_EXCLUDE"].split(",")
    if "RA_TAGS" in os.environ:
        config.setdefault("filters", {})["include_tags"] = os.environ["RA_TAGS"].split(",")
    if "RA_TRACE_TAIL" in os.environ:
        config.setdefault("artifacts", {})["trace_tail_events"] = int(os.environ["RA_TRACE_TAIL"])
    return config

def _env_bool(var: str, default: bool) -> bool:
    val = os.environ.get(var)
    if val is None:
        return default
    return val.lower() in ("1", "true", "yes", "on")
