# Part 2: Creating the List of Question Objects from the Data

from question_model import Question
from data import question_data

question_bank = []
for i in question_data:
    text = i["text"]
    answer = i["answer"]
    question = Question(text, answer)
    question_bank.append(question)

# def printingthequestionbank():
#     for t in question_bank:
#         print(t.enterquestion, t.theanswer)
# printingthequestionbank()

# for t in question_bank:
#     print(t.enterquestion, t.theanswer)

# print(question_bank[0].enterquestion, question_bank[0].theanswer)






