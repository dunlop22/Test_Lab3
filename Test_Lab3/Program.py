import msvcrt
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

            if (num_str == 4):
                game.AddRound(question, answers.copy(), answers[0])
                num_str = -2
                answers.clear()

            num_str += 1

        f.close()


class Game():
    def __init__(self):
        self.rounds = []
        self.score = 0
        self.question_number = 0

    def AddRound(self, question, answers, answer):
        self.rounds.append(Round(question, answers.copy(), answer))

    def GetRounsNumber(self):
        return len(self.rounds)

    def MixQuestions(self, questions):
        result = questions.copy()
        random.shuffle(result)
        return result

    def Start(self):
        self.score = 0
        self.question_number = 0
        questions = self.MixQuestions(self.rounds)

        for i in range(len(questions)):
            self.PrintHeader()
            self.question_number += 1

            questions[i].Print()
            answer = self.GetUserAnswer()
            print(answer)
            if (questions[i].CheckAnswer(questions[i].answers[answer - 1])):
                self.score += 1

                
    def GetUserAnswer(self):
        while True:
            answer = ord(msvcrt.getch()) - 48

            #Ответ на вопрос
            if (answer > 0 and answer < 5):
                return answer

            #Помощь (Help)
            if (answer == -21):
                self.ChooseHelp()
                return -1

                
    def ChooseHelp(self):
        while True:
             numHelp = ord(msvcrt.getch())
             if (numHelp > 0 and numHelp < 4):
                 break

        #Помощь друга
        if (numHelp == 1):
            #Генерация случайного значения от 1 до 4
            pass
        #Помощь зала
        elif (numHelp == 2):
            #Процентное распределение для каждого вопроса (в сумме 4х значений - 100 единиц)
            pass
        #Выход из меню
        elif (numHelp == 3):
            pass
            #exit


    def PrintHeader(self):
        os.system('cls')
        print("Приветствуем вас в игре \"Кто хочет стать милиционером\"!")            
        print("Текущий счет: ", self.GetScore(), "/", self.GetRounsNumber(), sep = "")
        print("Вопрос №", self.question_number + 1, "\n", sep = "")

    def GetScore(self):
        return self.score

class Round():
    def __init__(self, question = "", answers = ["", "", "", ""], answer = ""):
        self.question = question
        self.answers = answers.copy()
        self.answer = answer

    def CheckAnswer(self, answer):
        return answer == self.answer

    def Print(self):
        print("Вопрос: ", self.question, end = "")
        random.shuffle(self.answers)

        for i in range (4):
            print("\n",(i + 1), ") ", self.answers[i][:len(self.answers[i]) - 1], end = "", sep='')

        print("\n\nВведите номер ответа: ", end = "")

def main():
    fileReader = FileReader()
    game = Game()

    filename = "questions.txt"

    if fileReader.CheckFileExist(filename):
        if (fileReader.CheckInfoInFile(filename)):
            fileReader.ReadQuestions(filename, game)
            game.Start()
        else:
            print("Файл с вопросами пуст! Поиграть не получится(")
    else:
        print("Файл с вопросами отсутсвует! Поиграть не получится(")

main()