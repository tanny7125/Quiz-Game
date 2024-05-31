class QuizBrain:
    def __init__(self,q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_num < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.q_num]
        self.q_num +=1
        user_answer = input(f"Q.{self.q_num}: {item.text} (True/false):")
        self.check_answer(user_answer,item.answer)

    def check_answer(self,user,answer):
        if user.lower() == answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it Wrong")
        print(f"The correct answer to the question is {answer}.")
        print(f"Your score is {self.score}/{self.q_num}.")

