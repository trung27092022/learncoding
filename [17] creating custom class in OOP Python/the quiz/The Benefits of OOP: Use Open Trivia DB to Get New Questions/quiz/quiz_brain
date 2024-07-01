from main import question_bank

import os

question_number = 0
point = 0

class QuizBrain:
    # def __init__(self):
    #     pass
    def next_question(self):
        global question_number, point
        for i in question_bank:
            question_number = question_number + 1
            while 1<2:
                print(i.enterquestion)
                useranswer = input("Please enter your answer: ")
                if useranswer.capitalize() == "True" or useranswer.capitalize() == "False":
                    if useranswer.capitalize() == i.theanswer:
                        point += 1
                        print("  ")
                        print("You're correct! Your point is " + str(point) + "/" + str(question_number))
                        print("  ")
                        input("Press anything to continue.")
                        os.system('clear')
                    else:
                        print("  ")
                        print("You're incorrect! " + "The correct answer is: " + i.theanswer)
                        print("Your point is " + str(point) + "/" + str(question_number))
                        print("  ")
                        input("Press anything to continue...")
                        os.system('clear')
                    if question_number == len(question_bank):
                        print(" ")
                        print("Please enter anything to continue..")
                        input()
                        print("You've reached the end. " + "Your point is " + str(point) + "/" + str(question_number) + ". Thank you for playing!")
                        input()
                    break
                else:
                    print("  ")
                    print("Please reentry again!")
                    print("  ")
                    input("Press anything to continue.")
                    os.system('clear')

# QuizBrain.next_question('QuizBrain')


quizbrain = QuizBrain()

quizbrain.next_question()










