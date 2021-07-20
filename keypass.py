import random

print ("STRONG PASSWORD GENERATOR\n")
print ("Tool By www.github.com/varunherlekar\n")
print ("<===[[ coded by Varun Herlekar]]===>")

length=int(input("Enter The Length Of The Password: \n"))
print ("-----> Your Password Is Generated <----\n")
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password = "".join(random.choices(char,k=length))
print(password)
print ("-----> Copy The Password. Thank You For Using .<----\n")
print ("-----> Tool Created For WAP STTP Program.<----\n")
