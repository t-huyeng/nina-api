"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.version import Version

from deutschland import nina

globals()["Version"] = Version
from deutschland.nina.model.version_collection import VersionCollection


class TestVersionCollection(unittest.TestCase):
    """VersionCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVersionCollection(self):
        """Test VersionCollection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VersionCollection()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
