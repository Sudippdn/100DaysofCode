student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
for marks in student_scores:
  print(marks)
  if student_scores[marks]>90 and student_scores[marks]<100:
    print("A+")
  elif student_scores[marks]>80 and student_scores[marks]<90:
    print("A")
  elif student_scores[marks]>70 and student_scores[marks]<80:
    print("B+")
  elif student_scores[marks]>60 and student_scores[marks]<70:
    print("B")
  elif student_scores[marks]>50 and student_scores[marks]<60:
    print("C+")
  elif student_scores[marks]>40 and student_scores[marks]<50:
    print("C")
  elif student_scores[marks]<90:
    print("fail")