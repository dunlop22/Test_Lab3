import os

class FileReader():
    #todo ������� ������� � ������
    def CheckFileExist(self, filename):        
        return os.path.isfile(filename)

    def CheckInfoInFile(self, filename):
        return os.stat(filename).st_size != 0

class Game():
    def mixQuestions(self, questions):
        result = [i + 1 for i in range(len(questions))]
        return result