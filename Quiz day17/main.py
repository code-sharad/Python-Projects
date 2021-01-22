from question_model import Question, new_q
from data import question_data

question_bank = []


for i in range(7):
    question_bank += question_data[i]["text"] + "\n"

question_data[-1]["text"] += new_q.text
question_data[-1]["answer"] += new_q.answer

print(question_bank)


for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0])

