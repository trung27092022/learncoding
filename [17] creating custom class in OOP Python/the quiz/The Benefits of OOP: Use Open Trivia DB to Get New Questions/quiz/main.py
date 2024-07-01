# Part 2: Creating the List of Question Objects from the Data

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

# def printingthequestionbank():
#     for t in question_bank:
#         print(t.enterquestion, t.theanswer)
# printingthequestionbank()

# for t in question_bank:
#     print(t.enterquestion, t.theanswer)

# print(question_bank[0].enterquestion, question_bank[0].theanswer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")








