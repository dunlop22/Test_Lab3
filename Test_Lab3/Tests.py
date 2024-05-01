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
        
    def testCheckFileDoesNotExist(self):
        filereader = FileReader()
        result = filereader.CheckFileExist("")
        self.assertEqual(result, False)

    def testCheckFileDoesNotExistAfterRemove(self):
        #Создание файла
        open("test.txt", "w").close()
        filereader = FileReader()
        os.remove("test.txt")
        result = filereader.CheckFileExist("test.txt")
        self.assertEqual(result, False)