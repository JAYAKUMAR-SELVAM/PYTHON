# bitwise operater

"""
& and
| or
^ xor
~ not (~a becomes -a+1)
<< zero fill left shift (add two zero in right side)
>> signedbright shift (move two bit in right side)

"""
a=12
b=13

" and &"
print(a&b)

" | or"
print(a|b)

"^ xor"
print(a^b)

"~ not" 
print(~b)
print(~a)

"<< zero fill left shift"
print(a<<2)
print(b<<2)

">> signedbright shift"
print(a>>2)
print(b>>2)