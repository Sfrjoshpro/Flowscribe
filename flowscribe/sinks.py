"""
Sinks for outputting events to console and JSONL file.
"""
import json
from typing import Any
from .core import Event

class ConsoleSink:
    def write(self, event: Event):
        print(f"[{event.timestamp.isoformat()}] {event.event_type.upper()} | Flow: {event.flow_id} | Step: {event.step or '-'} | Tags: {event.tags} | Evidence: {event.evidence}")

class JSONLSink:
    def __init__(self, path: str):
        self.path = path

    def write(self, event: Event):
        with open(self.path, 'a', encoding='utf-8') as f:
            json.dump({
                'timestamp': event.timestamp.isoformat(),
                'event_type': event.event_type,
                'flow_id': event.flow_id,
                'step': event.step,
                'tags': event.tags,
                'evidence': event.evidence,
                'data': event.data
            }, f)
            f.write('\n')
