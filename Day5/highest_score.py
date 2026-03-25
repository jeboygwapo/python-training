student_scores = [150, 130, 22, 122, 190, 188, 211, 51]

# Getting the sum
total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

# Getting highest number
print(max(student_scores))

highest = 0
for score in student_scores:
    if score > highest:
        highest = score

print(highest)
