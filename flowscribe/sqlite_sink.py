"""
SQLite sink for flowscribe events (optional).
"""
import sqlite3
from .core import Event
from typing import Optional

class SQLiteSink:
    def __init__(self, path: str = ".autodev/trace.db"):
        self.path = path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    event_type TEXT,
                    flow_id TEXT,
                    step TEXT,
                    tags TEXT,
                    evidence TEXT,
                    data TEXT
                )
            ''')

    def write(self, event: Event):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT INTO events (timestamp, event_type, flow_id, step, tags, evidence, data) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    event.timestamp.isoformat(),
                    event.event_type,
                    event.flow_id,
                    event.step,
                    ",".join(event.tags),
                    str(event.evidence),
                    str(event.data)
                )
            )
