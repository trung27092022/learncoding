class Question:
    def __init__(self, question, answer):
        self.enterquestion = question
        self.theanswer = answer


question1 = Question("2+3", "True")

print(question1.theanswer)
