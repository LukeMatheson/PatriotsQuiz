class Question:

    def __init__(self, question, option1, option2, option3, option4, answer):
        self.__question = question
        self.__choice1 = option1
        self.__choice2 = option2
        self.__choice3 = option3
        self.__choice4 = option4
        self.__answer = answer

    def getQuestion(self):
        return self.__question

    def getOption1(self):
        return self.__option1

    def getOption2(self):
        return self.__option2

    def getOption3(self):
        return self.__option3

    def getOption4(self):
        return self.__option4

    def getAnswer(self):
        return self.__answer

    def askQuestion(self):
        return self.__question + '\n1. ' + self.__choice1 + '\n2. ' + self.__choice2 + '\n3. ' + self.__choice3 + '\n4. ' + self.__choice4
