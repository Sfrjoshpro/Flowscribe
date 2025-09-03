"""
Flow catalog loader and utilities for flowscribe.
"""
import os
import yaml
from typing import Dict, Any, Optional, List

class FlowCatalog:
    def __init__(self, path: str = ".autodev/flows.yaml"):
        self.path = path
        self.catalog = self._load_catalog()
        self._validate_catalog()
        self._index = {flow['id']: flow for flow in self.catalog['flows'] if flow.get('enabled', True)}
        self.defaults = self.catalog.get('defaults', {})

    def _load_catalog(self) -> Dict[str, Any]:
        with open(self.path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _validate_catalog(self):
        ids = set()
        for flow in self.catalog.get('flows', []):
            if 'id' not in flow:
                raise ValueError(f"Flow missing required 'id': {flow}")
            if flow['id'] in ids:
                raise ValueError(f"Duplicate flow id: {flow['id']}")
            ids.add(flow['id'])
            if 'parent' in flow and flow['parent'] not in ids:
                # Allow parent to be defined later, but warn if missing at end
                pass
        # Final parent check
        all_ids = {flow['id'] for flow in self.catalog.get('flows', [])}
        for flow in self.catalog.get('flows', []):
            if 'parent' in flow and flow['parent'] not in all_ids:
                raise ValueError(f"Parent flow '{flow['parent']}' for flow '{flow['id']}' not found in catalog.")

    def get_flow(self, flow_id: str) -> Optional[Dict[str, Any]]:
        flow = self._index.get(flow_id)
        if not flow:
            return None
        # Merge defaults
        merged = dict(self.defaults)
        merged.update(flow)
        return merged

    def list_enabled_flows(self) -> List[Dict[str, Any]]:
        return list(self._index.values())

    def filter_flows_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        return [f for f in self._index.values() if tag in f.get('tags', [])]
