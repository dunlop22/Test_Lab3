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


    def testMixQuestions(self):
        temp = [n for n in range(10)]
        game = Game()

        result = game.mixQuestions(temp)

        self.assertNotEqual(temp, result)


    def testMixQuestionsCorrectNumberOfElems(self):
        temp = [n for n in range(10)]
        game = Game()

        result = len(game.mixQuestions(temp))

        self.assertEqual(len(temp), result)


    def testMixQuestionsNoSameValues(self):
        temp = [n for n in range(10)]
        game = Game()

        result = game.mixQuestions(temp)
        number = len(set(result))

        self.assertEqual(number, len(result))


    def testMixQuestionsCorrectValues(self):
        temp = [n for n in range(10)]
        game = Game()

        result = game.mixQuestions(temp)
        
        for item in temp:
            f = False

            for res in result:
                if item == res:
                    f = True
                    break

            self.assertEqual(f, True)


    def testGetRoundNumberZero(self):
        game = Game()
        result = game.GetRounsNumber()
        self.assertEqual(result, 0)


class TestRound(unittest.TestCase):

    def testRoundClassCreation(self):
        r = Round()
        self.assertIsNotNone(r)


    def testRoundCheckAnswerCorrect(self):
        rnd = Round("Вопрос", ["1", "2", "3", "4"], "2")
        result = rnd.CheckAnswer("2")
        self.assertEqual(result, True)


    def testRoundCheckAnswerIncorrect(self):
        rnd = Round("Вопрос", ["1", "2", "3", "4"], "2")
        result = rnd.CheckAnswer("3")
        self.assertEqual(result, False)


    def testRoundCheckAnswerNoAnswer(self):
        rnd = Round("Вопрос", ["1", "2", "3", "4"], "2")
        result = rnd.CheckAnswer("")
        self.assertEqual(result, False)