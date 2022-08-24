#!/usr/bin/python3
string = input("Enter string:")
for i in string:
    if(i.islower()):
        print("The number of lowercase characters{}".format(i))
