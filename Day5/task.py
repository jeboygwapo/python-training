
student_scores = [150, 130, 22, 122, 190, 188, 211, 51]

print(max(student_scores))

highest = 0
for score in student_scores:
    if score > highest:
        highest = score

print(highest)
