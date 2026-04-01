# Grade	Class
# A+	Outstanding
# A	    Excellent
# B	    Very Good
# C	    Good
# D	    Average
# E	    Pass
# F	    Fail

marks = float(input("Enter your percentage: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"

print("Your Grade:", grade)