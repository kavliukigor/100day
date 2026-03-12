student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
}
for i in student_scores:
    if student_scores[i]>=91:
        student_grades[i] = "Outstanding"
    elif student_scores[i]>=81:
        student_grades[i] = "Exceeds"
    elif student_scores[i]>=71:
        student_grades[i] = "Acceptable"
    elif student_scores[i]<70:
        student_grades[i] = "Fail"



