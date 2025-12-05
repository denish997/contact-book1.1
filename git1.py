sub=int(input("Enter number of subjects: "))
marks=[]


for i in range(sub):
    n=input(f"Enter {i+1} subject name: ")
    m=float(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)
total=sum(marks)
per=total/sub

print("\n--- RESULT ---")
print("Total Marks:", total)
print("Percentages:",per)

if per >=90:
    print("Grade: A")
elif per >=75:
    print("Grade: B")
elif per >=50:
    print("Grade: C")
else:
    print("Grade: Fail")
