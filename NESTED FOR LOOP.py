# NESTED FOR LOOP

"""
*
**
***
****
****
_______________________________________________________________

*****
****
***
**
*
-------------------------------------------------------------------

abcde
abcde
abcde
abcde
abcde

A-Z  65-90
a-z  97-122

"""


for i in range(6):
    for j in range(i):
        print(j)
    print("")

print("------------------------------------")

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")

print("------------------------------------")


for i in range(6,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("------------------------------------")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
    
print("------------------------------------")