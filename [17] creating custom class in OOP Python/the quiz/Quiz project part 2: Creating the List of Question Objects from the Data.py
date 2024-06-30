from question_model import Question
from data import question_data

question_bank = []
for i in question_data:
    text = i["text"]
    answer = i["answer"]
    question = Question(text, answer)
    question_bank.append(question)

print(question_bank[0])
