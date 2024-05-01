from .Program import *
import unittest
import os

class TestFileReader(unittest.TestCase):

    def testFileReaderClassCreation(self):
        filereader = FileReader()
        self.assertIsNotNone(filereader)

    
    def testCheckFileExist(self):
        #Создание файла
        open("test.txt", "w").close()
        filereader = FileReader()
        result = filereader.CheckFileExist("test.txt")
        os.remove("test.txt")
        self.assertEqual(result, True)