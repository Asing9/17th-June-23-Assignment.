''' 1. What is the role of try and exception block?
 handle the run time error so that the regular flow of the program can be done

2. What is the syntax for a basic try-except block?

try:
    print(1+'hi')
except:
    pass

3. What happens if an exception occurs inside a try block and there is no matching
except block?
try:
    print(1 + 'hi')

    interrupt the program because there is no except to handle the exception

4. What is the difference between using a bare except block and specifying a specific
exception type?


try:
    a = 10
    b = 0
    c = a / b
    print(c)
except Exception as e:
    print(e)

try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError as obj:
    print(obj)

Bare except block can catch all kind of Exceptions
on other hand specfic exception catch only that type of exceptions

5. Can you have nested try-except blocks in Python? If yes, then give an example.

    yes we can use nested try except blocks

try:
    a=10
    d=0
    c=a/b


except Exception as obj:
    print(obj)

6. Can we use multiple exception blocks, if yes then give an example.

7.Write the reason due to which following errors are raised:
a.EOFError
b.FloatingPointError
c.IndexError
d.MemoryError
e.OverflowError
f.TabError
g.ValueError

EOF Error : This occurs when we have asked the user for
    input but have not provided any input in the input box.
    We can overcome this issue by using try and except keywords in Python.

FloatingPointError  :

IndexError : - If the specified index does not exist in the list then the method will return an IndexError exception.

MemoryError : This error occurs when the program tries to allocate more memory than the system can provide.

OverflowError : -this occurs when an obtained value or result is larger than the declared operation or data type
in the program then this throws an overflow error indicating the value is exceeding the given or declared limit value.

TabError :-  problem with the indentation of your program, it either raises an exception called
IndentationError or TabError.

ValueError:- if we try to convert a string that does not represent integer to a integer using the int() function,
a valueError will be reaised


8. Write code for the following given scenario and add try-exception block to it.
a. Program to divide two numbers
b. Program to convert a string to an integer
c. Program to access an element in a list
d. Program to handle a specific exception
e. Program to handle any exception

a. Program to divide two numbers


try:
    num1 = int(input(" enter first no :"))
    num2 = int(input(" enter second no :"))
    if num1>num2 :
        ans=num1/num2
        print(ans)
    else:
        ans = num2/num1
        print(ans)
except Exception as e:
    print("divide with valid no.")


b. Program to convert a string to an integer


try:
    s= input("enter a string:")
    n= int(s)

    print(n)
except ValueError as e:
    print(e)


c. Program to access an element in a list


try:
    list1 = ['Ajay', 'Vijay', 'Sanjay', 'Dhananjay', 'Ranvijay', 'Sujoy', 'Jay', 'Jia', 'Jaya', 'Pia']
    a=int(input('enter index no for 0 to 9:'))
    if a==0:
        print(list1[0])
    elif a==1:
        print(list1[1])
    elif a==2:
        print(list1[2])
    elif a==3:
        print(list1[3])
    elif a==4:
        print(list1[4])
    elif a==5:
        print(list1[5])
    elif a==6:
        print(list1[6])
    elif a==7:
        print(list1[7])
    elif a==8:
        print(list1[8])
    elif a==9:
        print(list1[9])
    else:
        print("enter valid no")

except ValueError as e:
    print(e)

d. Program to handle a specific exception

try:
    a=10
    b=20
    c=a+b
    print(d)

except NameError:
    print('Check Program')

e. Program to handle any exception
'''

try:
    a=10
    b=20
    c=a+b
    print(d)

except Exception as e:
    print('Check Program',e)
