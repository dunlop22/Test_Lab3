import os
import random

class FileReader():
    #todo ������� ������� � ������
    def CheckFileExist(self, filename):        
        return os.path.isfile(filename)

    def CheckInfoInFile(self, filename):
        return os.stat(filename).st_size != 0

class Game():
    def mixQuestions(self, questions):
        result = questions.copy()
        random.shuffle(result)
        return result

class Round():
    def __init__(self, question = "", answers = ["", "", "", ""], answer = ""):
        #todo ���������� ����������
        self.answer = answer

    def CheckAnswer(self, answer):
        return answer == self.answer