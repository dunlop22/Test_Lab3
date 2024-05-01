from .Program import *
import unittest


class TestFileReader(unittest.TestCase):

    def testFileReaderClassCreation(self):
        filereader = FileReader()
        self.assertIsNotNone(filereader)