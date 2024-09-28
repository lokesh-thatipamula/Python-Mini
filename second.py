import random
import string
pass_len=int(input())
charValues=string.ascii_letters+string.digits+string.punctuation

#list comprehension
password1="".join([random.choice(charValues)for i in range(pass_len)])

password2=""
for i in range(pass_len):
    password2+=random.choice(charValues)

print("Suggested Password1 :",password1)
print("Suggested Password2 :",password2)