#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

print("Select Operation: ")
print("1: add")
print("2: subtract")
print("3: multiply")
print("4: divide")

choice=input("Enter choice 1/2/3/4: ")
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))

if choice=="1":
    print(num_1, "+", num_2, "=", add(num_1, num_2))

