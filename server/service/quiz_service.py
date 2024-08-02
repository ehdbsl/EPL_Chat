import pandas as pd
import random

# file_path = '../.././EPL_quiz.xlsx'
file_path = '/Users/gimdoyun/Desktop/프로젝트_EPL챗봇/EPL_quiz.xlsx'
def validate_sheetname(sheetname):

    try:
        pd.read_excel(file_path, sheet_name=sheetname)
        return True
    except ValueError:
        return False

def generate_random_quiz(sheetname="default_sheetname"):
    quiz_data = pd.read_excel(file_path, sheet_name=sheetname)
    row = quiz_data.sample().iloc[0]
    question = row['Question']
    correct_answer = random.choice(row['정답'].split(','))
    incorrect_answers = random.sample(row['오답'].split(','), 3)
    options = incorrect_answers + [correct_answer]
    random.shuffle(options)
    return {
        "question": question,
        "options": options,
        "answer": correct_answer
    }
