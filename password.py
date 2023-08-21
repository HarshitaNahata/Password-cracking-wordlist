#Wordlist is combination of characters that is used for cracking the password
from string import *

from itertools import product
#combinations is made from product function for making password

val=ascii_letters + digits + punctuation
#you get all the letters
#if you assign punctuation you get all the special characters,digits for numbers
for i in range(1,4):
    for j in product(val,repeat=i):
        word="".join(j)
        #txt file stores all the passwords that are appended one by one
        p=open("password.txt","a")
        p.write(word)
        p.write("\n")