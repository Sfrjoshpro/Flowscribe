"""
Core event, flow, and session classes for flowscribe.
"""
from typing import Any, Dict, List, Optional
from datetime import datetime
import uuid

class Event:
    def __init__(self, event_type: str, flow_id: str, step: Optional[str] = None, 
                 data: Optional[Dict[str, Any]] = None, tags: Optional[List[str]] = None, 
                 evidence: Optional[Dict[str, Any]] = None, timestamp: Optional[datetime] = None):
        self.event_type = event_type  # e.g., checkpoint, success, failure, exception, metric, summary
        self.flow_id = flow_id
        self.step = step
        self.data = data or {}
        self.tags = tags or []
        self.evidence = evidence or {}
        self.timestamp = timestamp or datetime.utcnow()

class Flow:
    def __init__(self, flow_id: str, parent: Optional[str] = None, tags: Optional[List[str]] = None):
        self.flow_id = flow_id
        self.parent = parent
        self.tags = tags or []
        self.events: List[Event] = []

    def add_event(self, event: Event):
        self.events.append(event)

class Session:
    def __init__(self, app_name: str, mode: str = "default", tags: Optional[List[str]] = None):
        self.run_id = str(uuid.uuid4())
        self.app_name = app_name
        self.mode = mode
        self.tags = tags or []
        self.flows: Dict[str, Flow] = {}
        self.start_time = datetime.utcnow()
        self.end_time: Optional[datetime] = None

    def start_flow(self, flow_id: str, parent: Optional[str] = None, tags: Optional[List[str]] = None):
        flow = Flow(flow_id, parent, tags)
        self.flows[flow_id] = flow
        return flow

    def end_session(self):
        self.end_time = datetime.utcnow()
