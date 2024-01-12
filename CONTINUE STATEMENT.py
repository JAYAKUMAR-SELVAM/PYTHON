# CONTINUE STATEMENT (whlie loop using if condition)

print("............getting of odd numbers.....")
i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue
    print(i)
    i=i+1
    
print("............getting of even numbers.....")

i=1
while i<=20:
    if i%2 !=0:
        i=i+1
        continue
    print(i)
    i=i+1