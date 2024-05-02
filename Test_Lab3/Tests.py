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


    def testReadQuestionsCheckNumberTwo(self):
        game = Game()
        fileReader = FileReader()

        temp = open("test.txt", "w")
        for _ in range(12):
            temp.write("Hello world\n")
        temp.close()

        fileReader.ReadQuestions("test.txt", game)
        result = game.GetRounsNumber()

        os.remove("test.txt")

        self.assertEqual(result, 2)


    def testReadQuestionsCheckNumberZero(self):
        game = Game()
        fileReader = FileReader()

        temp = open("test.txt", "w")
        temp.close()

        fileReader.ReadQuestions("test.txt", game)
        result = game.GetRounsNumber()

        os.remove("test.txt")

        self.assertEqual(result, 0)



class TestGame(unittest.TestCase):

    def testGameClassCreation(self):
        game = Game()
        self.assertIsNotNone(game)


    def testMixQuestions(self):
        temp = [n for n in range(10)]
        game = Game()

        result = game.MixQuestions(temp)

        self.assertNotEqual(temp, result)


    def testMixQuestionsCorrectNumberOfElems(self):
        temp = [n for n in range(10)]
        game = Game()

        result = len(game.MixQuestions(temp))

        self.assertEqual(len(temp), result)


    def testMixQuestionsNoSameValues(self):
        temp = [n for n in range(10)]
        game = Game()

        result = game.MixQuestions(temp)
        number = len(set(result))

        self.assertEqual(number, len(result))


    def testMixQuestionsCorrectValues(self):
        temp = [n for n in range(10)]
        game = Game()

        result = game.MixQuestions(temp)
        
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


    def testGetRoundNumberTwo(self):
        game = Game()
        game.AddRound("Вопрос 1", ["1", "2", "3", "4"], "1")
        game.AddRound("Вопрос 2", ["1", "2", "3", "4"], "2")

        result = game.GetRounsNumber()
        self.assertEqual(result, 2)


    def testStartScoreIsZero(self):
        game = Game()
        game.Start()

        result = game.GetScore()
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