import msvcrt
import os
import random
import time

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
    zvanie = ["Рядовой полиции", "Младший сержант полиции", "Сержант полиции", "Старший сержант полиции", "Старшина полиции", "Прапорщик полиции", "Старший прапорщик полиции", "Младший лейтенант полиции", "Лейтенант полиции", "Старший лейтенант полиции", "Капитан полиции", "Майор полиции", "Подполковник полиции", "Полковник полиции"]
    helpText = ["Звонок другу", "Помощь зала", "50/50"]

    def __init__(self):
        self.rounds = []
        self.score = 0
        self.question_number = 0
        self.clues = [0 for _ in range(3)]
        
    def AddRound(self, question, answers, answer):
        self.rounds.append(Round(question, answers.copy(), answer))

    def GetRounsNumber(self):
        return len(self.rounds)

    def GetCluesNumber(self):
        result = 0

        for clueFlag in self.clues:
            if clueFlag == 0:
                result += 1
            elif clueFlag == 1:
                result = 0
                break

        return result

    def MixQuestions(self, questions):
        result = questions.copy()
        random.shuffle(result)
        return result

    def CheckResult(self):
        print("Игра окончена. Ваше звание:", Game.zvanie[self.GetScore()])

    def Start(self):
        self.score = 0
        self.question_number = 0
        questions = self.MixQuestions(self.rounds)

        i = 0

        while i < len(questions):
            self.PrintHeader()

            questions[i].Print()
            answer = self.GetUserAnswer()

            if answer != -1:
                print(answer)

                print("\n\nИ это", end = "", flush=True)
                for _ in range (5):
                    print(".", end = "", flush=True)
                time.sleep(0.5)

                if (questions[i].CheckAnswer(questions[i].answers[answer - 1])):
                    self.score += 1
                    print("\n\nПравильный ответ!   +1 очко ")
                    time.sleep(2)
                else:
                    print("\n\nОтвет неверный! Думайте лучше! ")
                    time.sleep(2)
                
                    self.question_number += 1
                    i += 1

        os.system('cls')
        print("Игра \"Кто хочет стать милиционером\" окончена!")            
        print("Ваш счет: ", self.GetScore(), "/", self.GetRounsNumber(), sep = "")
        self.CheckResult()
                
        
    def GetUserAnswer(self):
        while True:
            answer = ord(msvcrt.getch()) - 48

            #Ответ на вопрос
            if (answer > 0 and answer < 5):
                return answer

            #Помощь (Help)
            if (answer == -21 and self.GetCluesNumber() > 0):
                self.PrintHelpVariants()
                self.ChooseHelp()
                return -1
            
              
    def PrintHelpVariants(self):
        os.system('cls')
        print("Выберите вариант подсказки")

        i = 1

        for j in range(len(self.clues)):
            if (self.clues[j] == 0):
                print(i, "-", Game.helpText[j])
                i += 1

        print(i, "- Назад")


    def ChooseHelp(self):
        n = self.GetCluesNumber()

        while True:
             numHelp = ord(msvcrt.getch()) - 48
             if (numHelp > 0 and numHelp < n + 2):
                 break

        k = 1

        for i in range(len(self.clues)):
            if self.clues[i] == 0:
                if numHelp == k:
                    self.clues[i] = 1
                    numHelp = i + 1
                    break
                else:
                    k += 1
                    
        #Помощь друга
        if (numHelp == 1):
            #Генерация случайного значения от 1 до 4
            pass
        #Помощь зала
        elif (numHelp == 2):
            #Процентное распределение для каждого вопроса (в сумме 4х значений - 100 единиц)
            pass
        #50 на 50
        elif (numHelp == 3):
            pass
        #Выход из меню
        elif (numHelp == 4):
            pass
            #exit


    def PrintHeader(self):
        os.system('cls')
        print("Приветствуем вас в игре \"Кто хочет стать милиционером\"!")            
        print("Текущий счет: ", self.GetScore(), "/", self.GetRounsNumber(), sep = "")
        print("Вопрос №", self.question_number + 1, sep = "", end='')
        if self.GetCluesNumber() > 0:
            print("    Для подсказки нажмите ESC", end='')

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
        print("\n\nВопрос: ", self.question, end = "")
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