import tempfile
import unittest
from pathlib import Path
from main import analyze

class ConfigPrecedenceTests(unittest.TestCase):
    def test_later_file_wins_and_records_source(self):
        with tempfile.TemporaryDirectory() as folder:
            low = Path(folder) / "low"
            high = Path(folder) / "high"
            low.write_text("[core]\neditor = nano\n", encoding="utf-8")
            high.write_text("[core]\neditor = vim\n", encoding="utf-8")
            effective, history = analyze([low, high])
            self.assertEqual(effective[0]["value"], "vim")
            self.assertEqual(effective[0]["source"], str(high))
            self.assertEqual(len(history), 1)
