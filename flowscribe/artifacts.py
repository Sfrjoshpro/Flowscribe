"""
Artifact writers for summary.md, ask.md, and trace.jsonl
"""
import os
from typing import List
from .core import Session, Flow, Event

class ArtifactWriter:
    def __init__(self, base_dir: str = ".autodev", run_id: str = None):
        self.base_dir = base_dir
        self.run_id = run_id
        self.run_dir = os.path.join(base_dir, "runs", run_id) if run_id else base_dir
        os.makedirs(self.run_dir, exist_ok=True)

    def write_summary(self, session: Session):
        path = os.path.join(self.run_dir, "summary.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Run Summary\n\n")
            f.write(f"Run ID: {session.run_id}\nMode: {session.mode}\nTags: {session.tags}\nStart: {session.start_time}\nEnd: {session.end_time}\n\n")
            f.write("## Flows\n")
            for flow in session.flows.values():
                f.write(f"- {flow.flow_id} (parent: {flow.parent})\n")
            f.write("\n## Failures\n")
            for flow in session.flows.values():
                for event in flow.events:
                    if event.event_type == "failure":
                        f.write(f"- {flow.flow_id}: {event.evidence} at {event.timestamp}\n")
            # Add more sections as needed

    def write_ask(self, session: Session):
        path = os.path.join(self.run_dir, "ask.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write("# Copilot Ask Prompt\n\n")
            f.write(f"Run ID: {session.run_id}\nMode: {session.mode}\nTags: {session.tags}\n\n")
            f.write("## Flow Graph\n")
            for flow in session.flows.values():
                f.write(f"- {flow.flow_id}: {len(flow.events)} events\n")
            f.write("\n## Top Issues\n")
            for flow in session.flows.values():
                for event in flow.events:
                    if event.event_type == "failure":
                        f.write(f"- {flow.flow_id}: {event.evidence} at {event.timestamp}\n")
            f.write("\n## Evidence\n")
            for flow in session.flows.values():
                for event in flow.events:
                    if event.evidence:
                        f.write(f"- {flow.flow_id}: {event.evidence}\n")
            f.write("\n## Trace Excerpt\n")
            for flow in session.flows.values():
                for event in flow.events[-5:]:
                    f.write(f"- {event.event_type} {event.step or ''} {event.evidence} at {event.timestamp}\n")
            f.write("\n## Action Request\nPlease diagnose the first failure(s), propose a minimal patch, and add a test.\n")

    def write_trace(self, events: List[Event]):
        path = os.path.join(self.run_dir, "trace.jsonl")
        with open(path, "a", encoding="utf-8") as f:
            for event in events:
                f.write(event_to_jsonl(event) + "\n")

def event_to_jsonl(event: Event) -> str:
    import json
    return json.dumps({
        "timestamp": event.timestamp.isoformat(),
        "event_type": event.event_type,
        "flow_id": event.flow_id,
        "step": event.step,
        "tags": event.tags,
        "evidence": event.evidence,
        "data": event.data
    })
