import random 
import string
def generator(length,upper,lower,digit,special):
    passw=''
    if upper:
        passw+=string.ascii_uppercase
    if lower:
        passw+=string.ascii_lowercase
    if digit:
        passw+=string.digits
    if special:
        passw+=string.punctuation
    if not passw:
        return "Error:At least one character type must be selected"
    password="".join(random.choice(passw) for _ in range(length))
    return password
print("Welcome to password generator!")
length=int(input("enter length:"))
upper=input("upper case(y/n)").lower()=="y"
lower=input("lower case(y/n)").lower()=="y"
digit=input("digits (y/n)").lower()=="y"
special=input("special characters(y/n)").lower()=="y"
password=generator(length,upper,lower,digit,special)
print(f"generated password is {password}")


