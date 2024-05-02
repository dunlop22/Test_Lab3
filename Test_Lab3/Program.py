import os
import random

class FileReader():
    def CheckFileExist(self, filename):        
        return os.path.isfile(filename)

    def CheckInfoInFile(self, filename):
        return os.stat(filename).st_size != 0

    def ReadQuestions(self, filename, game):
        f = open(filename)
        num_str = 0

        answers = []

        for line in f:
            #Запись вопроса
            if num_str == 0:
                question = line

            #запись вариантов ответа
            elif (num_str > 0) and (num_str < 5):
                answers.append(line)

            num_str += 1

            if (num_str == 5):
                game.AddRound(question, answers.copy(), answers[0])
                num_str = 0
                answers.clear()

        f.close()


class Game():
    def __init__(self):
        self.rounds = []

    def AddRound(self, question, answers, answer):
        self.rounds.append(Round(question, answers.copy(), answer))

    def GetRounsNumber(self):
        return len(self.rounds)

    def mixQuestions(self, questions):
        result = questions.copy()
        random.shuffle(result)
        return result

class Round():
    def __init__(self, question = "", answers = ["", "", "", ""], answer = ""):
        #todo сохранение параметров
        self.answer = answer

    def CheckAnswer(self, answer):
        return answer == self.answer

def main():
    fileReader = FileReader()
    game = Game()

    filename = "questions.txt"

    if fileReader.CheckFileExist(filename):
        if (fileReader.CheckInfoInFile(filename)):
            fileReader.ReadQuestions(filename, game)
        else:
            print("Файл с вопросами пуст! Поиграть не получится(")
    else:
        print("Файл с вопросами отсутсвует! Поиграть не получится(")

main()