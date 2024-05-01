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


    def testCheckFileIsNotEmpty(self):
        temp = open("test.txt", "w")
        temp.write("Hello world")
        temp.close()

        filereader = FileReader()
        result = filereader.CheckInfoInFile("test.txt")
        os.remove("test.txt")

        self.assertEqual(result, True)

    def testCheckFileIsEmpty(self):
        open("test.txt", "w").close()

        filereader = FileReader()
        result = filereader.CheckInfoInFile("test.txt")
        os.remove("test.txt")

        self.assertEqual(result, False)

class TestGame(unittest.TestCase):
    def testGameClassCreation(self):
        game = Game()
        self.assertIsNotNone(game)