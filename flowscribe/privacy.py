"""
Redaction and payload limiting utilities for flowscribe.
"""
from typing import Any, Dict, List

REDACTED = "***REDACTED***"
TRUNCATED = "... (truncated)"

def redact_and_limit(data: Dict[str, Any], redact_keys: List[str], payload_limit: int) -> Dict[str, Any]:
    def _redact(obj):
        if isinstance(obj, dict):
            return {k: (REDACTED if k.lower() in redact_keys else _redact(v)) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [_redact(v) for v in obj]
        elif isinstance(obj, str) and len(obj) > payload_limit:
            return obj[:payload_limit] + TRUNCATED
        return obj
    return _redact(data)
