# NESTED IF STAYEMENT IN PYTHON (if ulla if)

"""
get 3 input(all 3 should be pass)
total
average

if all pass grade

   MARK         GRADE
   
  80-99           A
  70-80           B
  60-70           C
  50-60           D
  50-35           E
  BELOW 35      FAIL

"""
name=input("ENTER THE NAME : ")
n1=int(input("ENTER THE n1 MARK : "))
n2=int(input("ENTER THE n2 MARK : "))
n3=int(input("ENTER THE n3 MARK : "))
total=n1+n2+n3
average=total/3.0

print("TOTAL : ",total)
print(f"AVERAGE : {average}")

if n1>35 and n2>35 and n3>35:
    print(name,"u are passed")
    if average>=80 and average<=99:
        print(name,"your grade is A")
    elif average>=70 and average<=80:
        print(name,"your grade is B")
    elif average>=60 and average<=70:
        print(name,"your grade is C")
    elif average>=50 and average<=60:
        print(name,"your grade is D")
    else:
        print(name,"your grade is E")
else:
    print(name,"U ARE FAIL")
    