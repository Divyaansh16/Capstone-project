#password gemerator
import random
characters="abcdefghijklmnopqrstuvwxtzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456!@#$%^&*(){}:'[]-=/*-+ "
mypassword=int(input("Enter the lenght of the password: "))
password="".join(random.sample(characters,mypassword))
print(password)
