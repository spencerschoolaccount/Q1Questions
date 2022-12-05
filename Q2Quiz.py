totalQuestions = 0
totalScore = 0

def askquestion():
  fileName = input("What is the file named?\n")
  if fileName.endswith('.txt'):
    fileName = fileName[0:len(fileName)-4]
  inFile = open('questions/' + fileName + '.txt', 'r')
  content = inFile.readlines()
  while True:
    print('\n' + content[0] + '\n')
    print('A) ' + content[1])
    print('B) ' + content[2])
    print('C) ' + content[3])
    print('D) ' + content[4])
    
    userAnswer = input("\nEnter the correct answer (A, B, C, D):\n")
    if userAnswer.upper() != 'A' and userAnswer.upper() != 'B' and userAnswer.upper() != 'C' and userAnswer.upper() != 'D':
      print("Invalid answer, must be A, B, C, or D\n")
      continue
    elif userAnswer.upper() == content[5].strip('\n'):
      print('\nCorrect!\n')
      global totalScore
      totalScore = totalScore + 1
      break
    else:
      print('\nIncorrect, the answer was: ' + content[5].strip('\n') + '.\n')
      break
  inFile.close()
  global totalQuestions
  totalQuestions = totalQuestions + 1

while True:
  askquestion()
  if input("Is there another question? (Y/n) \n").lower() == 'n':
    print('')
    break
print("Your total score is: " + str(totalScore) + '/' + str(totalQuestions))
    