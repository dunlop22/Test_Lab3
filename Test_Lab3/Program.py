import os

class FileReader():
    #todo ��������� ������� �����, ������� ������� � ������
    def CheckFileExist(self, filename):        
        return os.path.isfile(filename)

    def CheckInfoInFile(self, filename):
        return True