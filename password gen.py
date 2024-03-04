import string
import random
s1 = string.ascii_lowercase
#print(s1)
s2=string.ascii_uppercase
#print(s2)
s3=string.digits
#print(s3)
s4=string.punctuation
#print(s4)
plen=int(input("Enter password length\n"))  #todo1:handle Gibbersish

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))   #append means list adds to previous list as a set;    #extend means elements will get added to previous list
#print(s)
random.shuffle(s)
#print(s)
print("Your password is: ");
print("".join(s[0:plen]))
