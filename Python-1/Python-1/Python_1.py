
x = [3,2]
print (x)

print("Hello")

x = "mystring"
print(x)

class Message1:
    pass
print(Message1)

# Defining the above as a process. Notice the difference in the class
# reported.

def MessageClassPrint():
    class Message:
        pass
    print (Message)
    return Message

Message = MessageClassPrint()

# Representing data
# This did not quite work as in the book as syntax is very different
# in current version of python (3.7) compared with python 2 

mytuple = (3, 4)
mylist = [1,"2", mytuple]
canonicallist =  repr(mylist)
print (canonicallist)

canonicallist == [1,"2", (3, 4)]

# Manipulating strings and lists

## printing commas and space

y = 'The meaning of life, the Universe and everything is'
x = 42
print (y,x)

## measuring things

x = 'blablablablablablablablablablabla'
length = len(x)
print (length)

## splitting strings - 3 lines

x = "This is a parrot!"
xsplit = x.split()
print (xsplit)

## or - 2 lines

ysplit = "This is a parrot!".split()
print (ysplit)

## or - 1 line

print("This is a parrot!".split())

# Getting help on a function

help(round)

print("Rounding 9.9... Result is", round(9.9))
print("Rounding 9.3... Result is",round(9.3))

# Examining names
dir()

# Examining a module

print(dir(__builtins__)) 
                  # The builtins module defines some exceptions 
                  # (error-handling code) functions and constants
                  
print(ArithmeticError)   
                  # The capitalised names in the builtins module are 
                  # exceptions, which you can see if you type one of 
                  # the names into interactive mode

# Writing multiline programs in interactive mode

# The following example program prints some km/mile conversions.

print("p.25 Writing multiline programs in interactive mode")
for miles in range (10,70, 10):
    km = miles * 1.609
    print("%d miles --> %3.2f kilometres" % (miles, km))


# p.29 Using Scripts and Modules

print ("Testing how scripts and interactive mode communicate")
x = 500
print ("The value of x is ", x)

# in a non-python environment type
# python -i tinysript.py
# to run this in interactive mode

#  p.30 importing a module in interactive mode

import tinymodule
# checking that the module's name has been imported - can you see element 
# tinymodule here?
print("Can you see element tinymodule in here?")
print(dir())

# in this example, we call th etinyfunction() attribute in the 
# tinymodule module and give a name to its result:

x = tinymodule.tinyfunction(2)
print (x)

# you can also import a specific function from within a module
# notes this method does not store the name of the module in the namespace

from tinymodule2 import tinyfunction2

# check 

print("Can you see element tinymodule2 in here? hint: you should")
print("Can you see tinymodule2 in here? hingt: you shouldn't")
print(dir())

