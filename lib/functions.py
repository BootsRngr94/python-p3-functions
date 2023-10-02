#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(Guido):
    print(f"Hello, {Guido}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

    #greet_with_default()
    #greet_with_default("Sunny")
    pass

def add(num1, num2):
    return num1 + num2
    

def halve(number):
    if not isinstance(number, (int,float)):
        return None

    return number / 2
