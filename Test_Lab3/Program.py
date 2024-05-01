import os

class FileReader():
    #todo проверить наличие файла, считать вопросы и ответы
    def CheckFileExist(self, filename):        
        return os.path.isfile(filename)

    def CheckInfoInFile(self, filename):
        return True