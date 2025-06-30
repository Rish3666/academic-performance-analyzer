subject1=(input("Enter name of the subject 1: "))
subject2=(input("Enter name of the subject 2: "))
subject3=(input("Enter name of the subject 3: "))
subject4=(input("Enter name of the subject 4: "))
subject5=(input("Enter name of the subject 5: "))
subject6=(input("Enter name of the subject 6: "))

try:
    
    marks1 = int(input(f"Enter Marks of {subject1}:" ))
    marks2 = int(input(f"Enter Marks of {subject2}:" ))
    marks3 = int(input(f"Enter Marks of {subject3}:" ))
    marks4 = int(input(f"Enter Marks of {subject4}:" ))
    marks5 = int(input(f"Enter Marks of {subject5}:" ))
    marks6 = int(input(f"Enter Marks of {subject6}:" ))

except:
    print("enter integers only!!")

try:
    tm1 = int(input(f"Total marks obtainable in {subject1}:" ))
    tm2 = int(input(f"Total marks obtainable in {subject2}:" ))
    tm3 = int(input(f"Total marks obtainable in {subject3}:" ))
    tm4 = int(input(f"Total marks obtainable in {subject4}:" ))
    tm5 = int(input(f"Total marks obtainable in {subject5}:" ))
    tm6 = int(input(f"Total marks obtainable in {subject6}:" ))

except:
    print("enter integers only!!")


tm = (tm1+tm2+tm3+tm4+tm5+tm6)

m1p = (marks1/tm1)*100
m2p = (marks2/tm2)*100
m3p = (marks3/tm3)*100
m4p = (marks4/tm4)*100
m5p = (marks5/tm5)*100
m6p = (marks6/tm6)*100

total_percentage = ((marks1+marks2+marks3+marks4+marks5+marks6)/tm)*100

total_percentage_required=int(input("Total percentage required to pass: "))

percentage_required=int(input("percentage required to pass per subject: "))


if   (m1p < percentage_required
   or m2p < percentage_required
   or m3p < percentage_required
   or m4p < percentage_required
   or m5p < percentage_required
   or m6p < percentage_required):
    print("You FAILED \n Better luck next time")

elif(total_percentage < total_percentage_required):
    print("You FAILED \n Better luck next time")

else:
    print("You have PASSED")

print(f"{subject1} percentage: {m1p}")
print(f"{subject2} percentage: {m2p}")
print(f"{subject3} percentage: {m3p}")
print(f"{subject4} percentage: {m4p}")
print(f"{subject5} percentage: {m5p}")
print(f"{subject6} percentage: {m6p}")

print("Your total percentage: ",total_percentage,"%")