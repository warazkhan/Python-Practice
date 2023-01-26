
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#Given a full name, your task is to capitalize the name appropriately.
#The string consists of alphanumeric characters and spaces.
#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.


import re 

def solve(s):
    regex_pattern = r"[^a-zA-Z0-9]"
    splitName= re.split(regex_pattern, s)

    for name in splitName:
        capitalWord = name.capitalize()
        s = s.replace(name, capitalWord)
    return s


if __name__ == '__main__':
    
    s = input()
    print(solve(s))