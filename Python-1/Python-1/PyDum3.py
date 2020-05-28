# PyDum3 - Python for Dummies chapter 3

# NAMING RULES

# names must start with either a letter or an underscore character
# can't use Python's reserved words or keywords
# names are case sensitive
# lowercase for names that stand for values
# use meaningful names

# STATEMENTS AND EXPRESSIONS

# a LITERAL specifies the value for one of the basic Python data types 
# (such as a string or number). When you run a program, Python creates
# an object with the literal's value

# a STATEMENT is like a command - it tells pythong to do something. 
# eg x = 25 is a statement and tells python to give the name x to 
# value 25 and print(x) tells python to display the value of x

# an EXPRESSION is one or more operations tha tproduce a result. Operations
# can involve names, operators, literals and function or method calls

# below an example

# this is an EXPRESSION and a LITERAL:

"monty python"
print("'monty python'")

#This is a STATEMENT. 25 is a LITERAL

x = 25
x

# This is also an EXPRESSION
2 in [1,2,3]

#This is a STATEMENT. return is a STATEMENT 1 is an EXPRESSION

def foo():
    return 1

# foo is a NAME  foo() is an EXPRESSION

foo()
print(foo())

# to see the type of a Python object use the type() function

type('foo')






