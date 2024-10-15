## Recap

Topics

1. Variables + Operators
2. Control flow statements - if, else, elif, for, while, match (switch statement)
3. Basic & Complex data types
4. Functions
5. List comprehension
6. Class and objects (OOP)
7. Libraries, modules

Basic - Scalar (single unit)
Complex - Aggregate (composite values)

Important traits of a list:


```
inventory = ["apple", "banana"]
```

string = 10 memory units
500 - 520
500-509 = "apple"
510-519 = "banana"

[0] = 500
[1] = 510

1. Items of a list are linear in memory. -> because of this indexing starts at 0. 
2. Python allows different types of data to be stored in a list [5, "video", True]

To open a terminal ctrl + `

Important traits of a dictionary:

1. Associates a key with a value. Useful for credentials (database), game objects
2. No duplicate keys. The latter value is "saved" in the dictionary
3. *Blazingly* fast

Important traits of a tuple:

To change something = to mutate something
unchangable = immutable 

1. Immutable data structure

Important traits of a set:

1. Doesn't allow duplicate elements


In the expression 2 + 5
+ is the operator
2, 5 are the operands

Types of operators:

18 / 12 = 1 reminder 6
(10 + 8) % 12 -> 6
12 % 12 = 0
13 % 12 = 1
12 * 2 = 24
24 % 12 = 0
26 / 12 = 2 || 12 * 2 = 24
reminder 2
26 % 12 = 2

1. Arithmetic operators -> +, -, *, /, // (integer division -> закръгля до цяло число), % (modulo), ** (power) 
!!! using + operator on strings will concatenate them (add them)
2. Logical operators -> not, and, or
equivalents in other languages: !, &&, ||
3. Comparison operators -> ==, <, >, <=, =>
4. Bitwise operator (побитови оператори) -> & (bit AND), | (bit OR), ^ (XOR), ~ (inverts all bits) 0010 -> 1101, << (left shift)>> (right shift)
5. Assignment operator: =, += (a += b is the same as a = a + b), -=, *=, /=, //=, %=, **=
6. Specific to python. Membership operators: in, not in
a = 5
l = [1, 2, 3, 4, 5, 6]
print(a in l) # -> True
print(a not in l) # -> False
7. Identity operator -> is, is not
== -> is the value the same?
is -> are the identities of the items the same?

Functions:

Functions are reusable pieces of code. 

Syntax:

Function definition (creation):

def <function_name>(<arg1>, <arg2>...):
    ...
    ...
    ...
    return <value>

Function invocation (извикване):

<function_name>(<arg1>...)
