question = input('What is your question?\n') + '\n'
answerA = input('\nWhat is Answer A?\n') + '\n'
answerB = input('\nWhat is Answer B?\n') + '\n'
answerC = input('\nWhat is Answer C?\n') + '\n'
answerD = input('\nWhat is Answer D?\n') + '\n'
correctAnswer = input('\nWhich is the correct answer? (A, B, C, D)\n').upper()
if correctAnswer != 'A' and correctAnswer != 'B' and correctAnswer != 'C' and correctAnswer != 'D':
  exit("Invalid correct answer, must be A, B, C, or D")

fileName = input("\nWhat would you like the file to be named?\n")
if fileName.endswith('.txt'):
  fileName = fileName[0:len(fileName)-4]
  print(fileName)
filehandle = open("questions/" + fileName + ".txt",'w')
filehandle.write(question + answerA + answerB + answerC + answerD + correctAnswer)
filehandle.close()