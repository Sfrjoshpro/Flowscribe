import unittest
import importlib
import sys

class TestMissingDependency(unittest.TestCase):
    def test_missing_pyyaml(self):
        # Simulate missing pyyaml by removing from sys.modules
        sys_modules_backup = dict(sys.modules)
        sys.modules['yaml'] = None
        try:
            with self.assertRaises(ImportError):
                importlib.reload(importlib.import_module('flowscribe'))
        finally:
            sys.modules.clear()
            sys.modules.update(sys_modules_backup)
