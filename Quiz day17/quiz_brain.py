from data import question_data

question_number = 0

# TODO asking the questions
question_number += 1
ask_q = input(f"Q{question_number} {question_data[1]['text']}(True/False)").upper()

# TODO: checking if the answer was correct
if ask_q == question_data[1]["answer"]:
    print("Right!")
else:
    print("Wrong!")
# TODO checking if we're the end of the quiz

print()