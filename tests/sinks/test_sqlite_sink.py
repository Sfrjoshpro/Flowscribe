import unittest
import os
from flowscribe.sqlite_sink import SQLiteSink
from flowscribe.core import Event
import sqlite3

class TestSQLiteSink(unittest.TestCase):
    def test_write_event(self):
        path = "test_trace.db"
        if os.path.exists(path):
            os.remove(path)
        sink = SQLiteSink(path)
        event = Event(event_type="metric", flow_id="test/flow", step="metric", evidence={"val": 42})
        sink.write(event)
        with sqlite3.connect(path) as conn:
            cur = conn.execute("SELECT event_type FROM events")
            row = cur.fetchone()
            self.assertEqual(row[0], "metric")
        os.remove(path)
