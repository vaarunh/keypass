import random, os, sys

print ("STRONG PASSWORD GENERATOR")
print (" ")
print ("Tool By www.github.com/varunherlekar")

print (" ")

print ("<===[[ coded by Varun Herlekar]]===>")

print (" ")


length=int(input("Enter The Length Of The Password: "))
print (" ")
print ("-----> Your Password Is Generated <----")
print (" ")
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password= (" ")
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print ("-----> Copy The Password. Thank You For Using .<----")
print ("-----> Tool Created For WAP STTP Program.<----")
print (" ")

