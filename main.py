from question_model import Question
from data import question_data
from quiz_brain import quiz_brain


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question( question_text, question_answer)
    question_bank.append(new_question)
quiz=quiz_brain(question_bank)
quiz.next_question()
while quiz.still_have_questions():
    quiz.next_question()
print("you have finished your quiz")
print(f"your score is {quiz.score}/{quiz.question_number}")

