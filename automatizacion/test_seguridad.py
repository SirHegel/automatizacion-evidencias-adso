"""Regresiones de los límites de confianza del automatizador."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("resolver_evidencias.py")
SPEC = importlib.util.spec_from_file_location("resolver_evidencias", MODULE_PATH)
assert SPEC and SPEC.loader
resolver = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = resolver
SPEC.loader.exec_module(resolver)


class PrivateBlocklistSecurityTests(unittest.TestCase):
    def test_rejects_an_absolute_external_path(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "solo admite"):
            resolver.load_private_terms(Path("/tmp/lista-externa.txt"))

    def test_rejects_relative_traversal_and_alternate_names(self) -> None:
        for candidate in (Path("../.privacidad.local"), Path("otra-lista.local")):
            with self.subTest(candidate=candidate):
                with self.assertRaisesRegex(RuntimeError, "solo admite"):
                    resolver.load_private_terms(candidate)


if __name__ == "__main__":
    unittest.main()
