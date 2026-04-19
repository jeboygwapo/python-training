import random
import pandas as pd
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# new_list = [n * 2 for n in range(1,5)]
# print(new_list)
#
# # Conditional List
# # new_list = [new_item for item in list if test]
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [n for n in names if len(n) <= 4]
# long_names = [n.upper() for n in names if len(n) > 4]
# print(long_names)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1,100) for student in names}
# passed_students = {student: score for student, score in student_scores.items() if score >= 60}
# print(student_scores)
# print(passed_students)

student_dict = {
    'student': ['angela', 'james', 'lily'],
    'score': [56, 76, 98]
}
# Looping through dictionaries
# for key, value in student_dict.items():
#     print(value)

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for key,value in student_data_frame.items():
#     print(key)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    if row.student == 'angela':
        print(row.score)