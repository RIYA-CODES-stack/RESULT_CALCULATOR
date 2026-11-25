#grade calculator
#enter marks 
#evaluate and calculate % 
#grade assign and position determine
#store all students marks in memory


print("========= RESULT CALCULATOR==========")
print("please enter all details listed below :")

#data to be taken from user
students_data = []

while True:
        NAME = input("ENTER THE NAME OF STUDENT :")
        ROLL_NO =input(f"Enter the Roll No. of {NAME} :")
        PHY = int(input("Enter the Marks in physics :"))
        CHE = int(input("Enter the Marks in Chemistry :"))
        MAT = int(input("Enter the Marks in Maths :"))
        COM = int(input("Enter the Marks in Computer :"))



        marks_scored = PHY + CHE + MAT + COM 
        total_marks = 400
        
        percentage = (marks_scored/total_marks)*100

        #Grade assign karna

        if 100>=percentage >=90 :
                grade ="A+"
        elif 90>= percentage >=80 :
                grade = "A"
        elif 80>= percentage >=70 :
                grade =  "B"
        elif 70 >= percentage >= 60 :
                grade = "C"
        elif 60>= percentage >=45 :
                grade =" D"
        else :
                grade = "FAIL"

        print(f"PERCENTAGE :{percentage}% | GRADE : {grade}")

        #ek student ka pura data in dictionary

        student = {
                "name" : NAME ,
                "ROLL_NO." : ROLL_NO ,
                "Marks" : marks_scored ,
                "PERCENTAGE" :percentage,
                "Grade" : grade
        }
        students_data.append(student)
        print(students_data)

        cond = input("add other students or not:");
        if cond.lower() == 'no':
                break

#==========sabka data print karna==========
print("\n========== ALL STUDENTS RESULT ===========")
for s in students_data:
        print(f"Name : {s['name']} | Roll :{s['ROLL_NO.']} |Marks :{s['Marks']}/400 | Percentage :{s['PERCENTAGE']}% | Grade :{s['Grade']} ")


#==============TOPPER NIKALNA ==============
Topper = max(students_data, key=lambda x:x["PERCENTAGE"])
print("\n=========== TOPPER ============")
print(f"{Topper['name']} has Scored {Topper['PERCENTAGE']}% with {Topper['Grade']} Grade")
print("Congratulations !")



        












    

    

    


