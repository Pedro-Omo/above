# score >= 90 = A, score >= 80 = B, score >= 70 = C, score >= 60 = D

print (" FIRST SEMESTER ASSESSMENT PORTAL ")

score = input(" Enter Student Score: ")
score = int(score)
if score >=90:
    grade = "A"
if score >=80:
  grade = "B"
if score >=70:
    grade = "C"
if score >=60:
    grade = "D"
if score >=50:
    grade = "E"
else:
 grade = "F"
                        
print (f"The score of student is {score} and grade is {grade}")
   