import unittest
import random
from ...Changelog import *
from ...__main__ import __version__

class VersionSearchTest(unittest.TestCase):
    def test_current(self):
        version = find_version_info(fullstr=__version__)
        self.assertIn(f"=== HubBase v{__version__}", version)

    def test_random(self):
        with open((Path(__file__).resolve().parent.parent.parent / "Data" / "versions.json"), "r") as f:
            for key in dict(json.load(f)).keys():
                if random.randint(1, 100) == 1: version = key; break
            else: version = "0.0.2.0.00"
        versioncont = find_version_info(fullstr=version)
        self.assertIn(f"=== HubBase v{version}", versioncont)