"""Offline regression tests for database configuration (no real credentials)."""
import os
from pathlib import Path
import runpy
import sys
import types
import unittest
from unittest.mock import Mock, patch

SOURCE = Path(__file__).resolve().parents[1] / "flask/db_config.py"


class ConfigTests(unittest.TestCase):
    def load_config(self, env):
        factory = Mock()
        module = types.ModuleType("supabase")
        module.create_client = factory
        with patch.dict(os.environ, env, clear=True), patch.dict(
            sys.modules, {"supabase": module}
        ):
            namespace = runpy.run_path(str(SOURCE))
        return factory, namespace

    def test_missing_url(self):
        with self.assertRaisesRegex(RuntimeError, "SUPABASE_URL"):
            self.load_config({})

    def test_missing_key(self):
        with self.assertRaisesRegex(RuntimeError, "SUPABASE_KEY"):
            self.load_config({"SUPABASE_URL": "https://example.invalid"})

    def test_whitespace_key(self):
        with self.assertRaisesRegex(RuntimeError, "SUPABASE_KEY"):
            self.load_config({
                "SUPABASE_URL": "https://example.invalid",
                "SUPABASE_KEY": "  ",
            })

    def test_configured_client_without_queries(self):
        factory, namespace = self.load_config({
            "SUPABASE_URL": " https://example.invalid ",
            "SUPABASE_KEY": " dummy-test-key ",
        })
        factory.assert_called_once_with("https://example.invalid", "dummy-test-key")
        self.assertIs(namespace["supabase"], factory.return_value)
        self.assertEqual(factory.return_value.mock_calls, [])


if __name__ == "__main__":
    unittest.main()
