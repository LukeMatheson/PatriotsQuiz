from QuestionClass import Question


def createObjects():
    for x in range(10):
        question = Question(questionsList[x], optionsList[x][0], optionsList[x][1], optionsList[x][2],
                            optionsList[x][3], answersList[x])
        objectsList.append(question)


questionsList = ['Who was the starting QB for the Patriots before Tom Brady?',
                 'In what 4 years did the Patriots win a Super Bowl?', 'In what round was Tom Brady drafted?',
                 'The Patriots released WR Wes Welker in 2013. What WR did the Patriots sign to replace him?',
                 'Who was the Patriots Hall of Famer who wore #54?',
                 'What 2 teams has Tom Brady lost to in the Super Bowl?', 'Who did the Patriots play in Super Bowl 52?',
                 'How many times has Tom Brady won the MVP award?',
                 'What was the name of the quarterback who took over when Brady tore his ACL?',
                 'Who scored the game-winning touchdown in overtime of Super Bowl 51 to complete the 28-3 comeback?',
                 'What year were the New England Patriots founded?',
                 'Which of the following Super Bowls did the New England Patriots NOT win?',
                 'How many years did it take Bill Belichick to win a Super Bowl with the New England Patriots?',
                 'In the seventh game of the 2004 season, the Patriots lost to make their record 6-1. Who did they play?',
                 'Where did Tom Brady go to college?'
                 
                 ]
optionsList = [['Matt Cassel', 'Drew Bledsoe', 'Brian Hoyer', 'Danny Etling'],
               ['2002, 2003, 2008, 2013', '2003, 2004, 2007, 2013', '2001, 2003, 2004, 2014', '2001, 2003, 2004, 2007'],
               ['1st', '3rd', '5th', '6th'], ['Randy Moss', 'Danny Amendolda', 'Julian Edelman', 'Brandin Cooks'],
               ["Dont'a Hightower", 'Rodney Harrison', 'Teddy Bruschi', 'Vince Wilfork'],
               ['Giants, Eagles', 'Giants, Panthers', 'Eagles, Rams', 'Falcons, Panthers'],
               ['Philadelphia Eagles', 'Atlanta Falcons', 'Los Angeles Rams', 'Carolina Panthers'],
               ['4 times', '5 times', '2 times', '3 times'],
               ['Jacoby Brissett', 'Matt Cassel', 'Brian Hoyer', 'Peyton Manning'],
               ['James White', 'Deion Lewis', 'Sony Michel', 'Stephen Ridley'],
               ['1940', '1950', '1960', '1970'],
               ['Super Bowl XXXVI', 'Super Bowl XXXVII', 'Super Bowl XXXVIII', 'Super Bowl XXXIX'],
               ['1', '2', '3', '4'],
               ['Denver Broncos', 'New York Jets', 'Chicago Bears', 'Pittsburgh Steelers'],
               ['Georgia', 'Ohio State', 'Michigan', 'LSU']
               
               ]
objectsList = []
answersList = [2, 3, 4, 2, 3, 1, 1, 4, 2, 1, 3, 2, 2, 4, 3]
player1 = 0
player2 = 0
index = 0
playerCount = 1

createObjects()
for z in range(10):
    print('Player', playerCount, 'here is your question:')
    print(objectsList[index].askQuestion())
    userInput = input('Enter your answer: ')
    while userInput != '1' and userInput != '2' and userInput != '3' and userInput != '4':
        print('Error: your answer here has to be a value between 1 and 4. Try again.')
        userInput = input('Enter your answer: ')
    answer = objectsList[index].getAnswer()
    if int(userInput) == answer:
        print('Excellent! You score!')
        if playerCount == 1:
            player1 += 1
        else:
            player2 += 1
    else:
        print('That is incorrect. Better luck with the next question.')
    if playerCount == 1:
        playerCount += 1
    else:
        playerCount -= 1
    index += 1
print('And the final scores are:')
print('Player 1:', player1)
print('Player 2:', player2)
if player1 > player2:
    print('Player 1 wins!')
elif player2 > player1:
    print('Player 2 wins!')
else:
    print("It's a tie!")
