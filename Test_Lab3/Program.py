import os
import random

class FileReader():
    #todo считать вопросы и ответы
    def CheckFileExist(self, filename):        
        return os.path.isfile(filename)

    def CheckInfoInFile(self, filename):
        return os.stat(filename).st_size != 0

class Game():
    def __init__(self):
        self.rounds = []

    def AddRound(self, question, answers, answer):
        self.rounds.append(Round(question, answers.copy(), answer))

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
    pass

main()