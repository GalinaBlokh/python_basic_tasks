#1.24.
'''1.24. Define a function `max()` that takes two numbers as
arguments and returns the largest of them. Use the if-then-else
 construct available in Python. (It is true that Python has the 
 `max()` function built in, but writing it yourself is 
 nevertheless a good exercise ). '''
def maximums(a, b):
    if a > b :
        return a
    else:
        return b

#1.25.
        '''
  Define a function `max_of_three()` that takes three numbers as 
  arguments and returns the largest of them.        
       '''
def max_of_three(a, b, c):
    maximum = maximums(maximums(a, b), c)
    return maximum
       
#1.26.
    '''
  Define a function that computes the length of a given list or
  string. ( It is true that Python has the `len()` function 
  built  in, but writing it yourself is nevertheless a good 
  exercise ).    
    '''
def length(list_or_str):
    count = 0
    for i in list_or_str:
        count += 1
    return count

#1.27.
    '''
 . Write a function that takes a character ( i.e. a string of length 1 ) and 
 returns `True` if it is a vowel, `False` otherwise   
    '''
def is_vowel(char):
    vowel = ('a', 'e', 'i', 'o', 'u')
    if char not in vowel:
        return False
    return True

#1.28   
    '''
  Write a function `translate()` that will translate a text 
  into "rövarspråket" (Swedish for "robber's language"). 
  That is, double every consonant and place an occurrence of 
  "o" in between. For example, `translate("this is fun")` should 
  return the string `"tothohisos isos fofunon".`    
    '''
def translater(st):
    new_st =''
    vol = (' ','a', 'e', 'i', 'o', 'u')
    for letter in st:
        if letter not in vol:
            new_st = new_st + letter + vol[-2] + letter
        else:
            new_st =new_st + letter
    print(new_st)
        
#2.1   
    '''
Write a program which will find all such numbers which are 
divisible by 7 but are not a multiple of 5, between 2000 and 
3200 (both included). The numbers obtained should be printed 
in a comma-separated sequence on a single line. Hints: Consider
 use range(#begin, #end) method    
    '''
def div_by_seven():
    list = []
    for n in range(2000, 3001):
        if n % 7 == 0 and n % 5 != 0:
            list.append(n)
    return list

#2.2
    '''
   Write a program which can compute the factorial of a given 
   numbers. The results should be printed in a comma-separated 
   sequence on a single line. Suppose the following input is 
   supplied to the program: 8 Then, the output should be: 40320 
   Hints: In case of input data being supplied to the question,
   it should be assumed to be a console input.
 
    '''
def factorial(n):
    n = int(input())
    factorial = 1
    if n == 0:
        return factorial
    for num in range(factorial, n+1):
        factorial = factorial*num
    return factorial

#2.3
    '''
    With a given integral number n, write a program to 
    generate a dictionary that contains (i, i*i) such that is 
    an integral number between 1 and n (both included). and then 
    the program should print the dictionary. Suppose the following
    input is supplied to the program: 8 Then, the output should 
    be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    Hints: In case of input data being supplied to the question, 
    it should be assumed to be a console input. Consider use 
    dict() 
    '''
def dictionary_of_sq():
    n = int(input())
    d = {i:i*i for i in range(1, n+1)}
    print(d)


#2.4 
    '''
    Write a program which accepts a sequence of comma-separated 
    numbers from console and generate a list and a tuple which 
    contains every number. Suppose the following input is supplied
    to the program: 34,67,55,33,12,98 Then, the output should be:
        ['34', '67', '55', '33', '12', '98'] 
        ('34', '67', '55', '33', '12', '98') 
        Hints: In case of input data being supplied to the 
        question, it should be assumed to be a console input. 
        tuple() method can convert list to tuple
    '''
def list_and_tuple():
    lst = input().split(',')
    print(lst)
    tpl = tuple(lst)
    print(tpl)

#2.5
    '''
    Write a method which can calculate a square value of a number 
    '''
def square(num):
    """Return the square value of the input number.
    The input number must be integer.
    """
    return num**2

#2.6
    '''
    Python has many built-in functions, and if you do not know 
    how to use it, you can read document online or find some books.
    But Python has a built-in document function for every 
    built-in functions. Please write a program to print some 
    Python built-in functions documents, such as abs(), int(),
    raw_input() And add document for your own function    
    Hints:    The built-in document method is __doc__ 
    '''
def docs_function():
    print (abs.__doc__)
    print (int.__doc__)
 #   print (raw_input.__doc__) undefined
    print (square.__doc__)

#2.7. class 
#Answer the follwing questions and write the following classes 
'''1. What is a class?
A class is a code template for creating objects.

2. What is an instance? 
An object which  is created using the constructor of the class.

3. What is encapsulation? 
Encapsulation is one of the fundamental concepts in 
object-oriented programming (OOP). It describes the idea of 
wrapping data and the methods that work on data within one unit.
 This puts restrictions on accessing variables and methods 
 directly and can prevent the accidental modification of data. 
 To prevent accidental change, an object’s variable can only 
 be changed by an object’s method Those type of variables 
 are known as private varibale.
A class is an example of encapsulation as it encapsulates all
 the data that is member functions, variables, etc.
 
4. What is inheritance? 
Inheritance is the capability of one class to derive or 
inherit the properties from some another class. The benefits 
of inheritance are:
It represents real-world relationships well.
It provides reusability of a code. We don’t have to write the 
same code again and again. Also, it allows us to add more 
features to a class without modifying it.
It is transitive in nature, which means that if class B inherits
 from another class A, then all the subclasses of B would 
 automatically inherit from class A.
 
5. What is polymorphism?
In literal sense, Polymorphism means the ability to take various 
forms. In Python, Polymorphism allows us to define methods in the 
child class with the same name as defined in their parent class.

'''
'''6. Traingle Class: 
    a. Create a class, Triangle. 
Its __init__() method should take self, angle1, angle2, a
nd angle3 as arguments.
 Make sure to set these appropriately in the body of the
 __init__()method. 
 b. Create a variable named number_of_sides and set it equal to 3.
 c. Create a method named check_angles. The sum of a triangle's
 three angles is It should return True if the sum of self.angle1, 
 self.angle2, and self.angle3 is equal 180, and False otherwise. 
 d. Create a variable named my_triangle and set it equal to a new 
 instance of your Triangle class. Pass it three angles that sum
 to 180 (e.g. 90, 30, 60). 
 e. Print out my_triangle.number_of_sides and print out 
 my_triangle.check_angles(). '''

class Triangle(object):
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

'''
7. Songs class:
a. Define a class called Songs, it will show the 
    lyrics of a song. Its __init__() method should have two 
    arguments:selfanf lyrics. Lyrics is a list. Inside your class 
    create a method called sing_me_a_songthat prints each element 
    of lyrics on his own line. Define a varible: 
b. happy_bday = Song(["May god bless you, ",                   
    "Have a sunshine on you,",                   
    "Happy Birthday to you !"]) 
c. Call the sing_me_song method on this variable 
'''
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_songthat(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["May god bless you, ",                   
                   "Have a sunshine on you,",                   
                   "Happy Birthday to you !"]) 
print(happy_bday.sing_me_a_songthat())    
    
'''
8. Define a class called Lunch. Its __init__() method should have 
two arguments:selfanf menu.Where menu is a string. Add a method 
called menu_price.It will involve a if statement: if "menu 1" 
print "Your choice:", menu, "Price 12.00", if "menu 2" 
print "Your choice:", menu, "Price 13.40", else print 
"Error in menu".   To check if it works define: 
    Paul=Lunch("menu 1") and call Paul.menu_price().
'''
class Lunch(object):
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1": 
            print ("Your choice:", self.menu, "Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice:", self.menu, "Price 13.40")
        else:
            print ("Error in menu")
            
Paul=Lunch("menu 1")
Paul.menu_price()

'''
9. Define a Point3D class that inherits from object Inside the 
Point3D class, define an __init__() function that accepts 
self, x, y, and z, and assigns these numbers to the member 
variables self.x,self.y,self.z. Define a __repr__() method 
that returns "(%d, %d, %d)" % (self.x, self.y, self.z). 
This tells Python to represent this object in the following format:
    (x, y, z).
 Outside the class definition, create a variable named my_point 
 containing a new instance of Point3D with x=1, y=2, and z=3.
 Finally, print my_point. You can find the solutions to these 
 exercises in the link: 
     https://erlerobotics.gitbooks.io/
     erle-robotics-learning-python-gitbookfree/classes/
     exercisesclasses.html
'''
class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print(my_point)

'''
2.8 List comprehension -  a quick reminder 
1. Use dictionary 
comprehension to create a dictionary of numbers 1- 100 to their 
squares (i.e. {1:1, 2:4, 3:9 …} 
'''
def comprehention_dictionary():
    n = {a:a**2 for a in range(1, 101)}
    print(n)
    
    '''
2. Use list comprehension to create 
a list of prime numbers in the range 1100 
http://www.secnetix.de/olli/Python/list_comprehensions.hawk 
    '''
def comprehention_list():
    prime_list = [a for a in range(1, 1101) 
                    if all(a%y != 0 for y in range(2, a))]
    print(prime_list)

'''
2.9. Files Use open, read, write, close which are explained in 
these tutorials:
https://www.tutorialspoint.com/python/python_files_io.htm 
https://www.guru99.com/reading-and-writing-files-in-python.html
 to: 
    1. Write “Hello world” to a file 
    2. Read the file back into python. 
    3. Write the square roots of the numbers 1-100 into the file, 
    each in new line. 
'''
def files_ex():
    file = open("testfile.txt", "w")
    file.write('Hello world \n')
    file.write('This is our new text file \n') 
    file.write('and this is another line.\n') 
    file.write('Why? Because we can\n') 
    file.close()
    
    file = open('testfile.txt', 'r')
    #print(file.read())
    #file = open('testfile.txt', 'r')
    print(file.readlines())
    
    file = open("testfile.txt", "w")
    for i in range(1,101):
        file.write(str(i**2)+'\n')
    file.close()
    
    file = open('testfile.txt', 'r')
    print(file.readlines())

'''
2.10
With
Read about with in one of the following links:
https://stackoverflow.com/questions/1369526/what-is-
the-python-keywordwith-used-for
http://effbot.org/zone/python-with-statement.htm
1. Open a file using with and write the first paragraph from 
(you don’t need
to read the webpage, just copy paste it into code)
https://en.wikipedia.org/wiki/Eigenface
2. Open the file using with and read the contents using 
readlines.
'''
def open_close_with():
    with open('output.txt', 'w') as fi:
        fi.write('''Eigenfaces is the name given to a set of 
             eigenvectors when they are used in the computer 
             vision problem of human face recognition.[1] The
             approach of using eigenfaces for recognition was 
             developed by Sirovich and Kirby (1987) and used 
             by Matthew Turk and Alex Pentland in face 
             classification.[2] The eigenvectors are derived
             from the covariance matrix of the probability 
             distribution over the high-dimensional vector 
             space of face images. The eigenfaces themselves 
             form a basis set of all images used to construct
             the covariance matrix. This produces dimension 
             reduction by allowing the smaller set of basis 
             images to represent the original training images.
             Classification can be achieved by comparing how 
             faces are represented by the basis set.''')
        fi.close()
    
    with open('output.txt', 'r') as f:
        print(f.readlines())
    f.close()

'''
2.11.
Strings
1. Split the paragraph to a list of words by spaces 
(hint: split()) 
2. Join the words back into a long string using “join”. 
(hint: join())
* (optional) Create a paragraph with the word order reversed
 in each sentence (but keep the order of the sentences)
3. write a function accepting two numbers and printing 
“the sum of __ and ___ is ___”.
Do this twice using one string formats learned in class each
 time.
Hint: https://pyformat.info/
'''

def spliting():
    s = '''Eigenfaces is the name given to a set of 
             eigenvectors when they are used in the computer 
             vision problem of human face recognition.[1] The
             approach of using eigenfaces for recognition was 
             developed by Sirovich and Kirby (1987) and used 
             by Matthew Turk and Alex Pentland in face 
             classification.[2] The eigenvectors are derived
             from the covariance matrix of the probability 
             distribution over the high-dimensional vector 
             space of face images. The eigenfaces themselves 
             form a basis set of all images used to construct
             the covariance matrix. This produces dimension 
             reduction by allowing the smaller set of basis 
             images to represent the original training images.
             Classification can be achieved by comparing how 
             faces are represented by the basis set.'''
    a = s.split()
    print(a)
    b = ' '.join(a)
    print(b)
    
def formating(a,b):
    c = a+b
    print('the sum of {} and {} is {}'.format(a,b,c))
    
'''
2.12.
Datetime, time, timeit
Read the current datetime to a variable usint 
datetime.datetime.no see:
https://docs.python.org/3/library/datetime.html
10. Print the date of the day before yesterday, and the
 datetime in 12 hours
from now
Use time library to time library to time operations by 
storing time.time()
before and after running an operation
https://www.tutorialspoint.com/python/time_time.htm
1. Time one of the comprehension exercises you’ve performed
 and compare
to a simple for implementation, to determine which one is
 faster
1. Now use timeit library to time your list comprehension 
operation, see:
https://docs.python.org/2/library/timeit.html

'''
def timing1():
    from datetime import date, timedelta
    import time
    
    start = time.time()
    
    yesterday = date.today() - timedelta(days=1)
    print(yesterday.strftime('%Y-%m-%d'))
    end = time.time()
    execution_time = end-start
    print(execution_time)
    
def timing2(): 
    from datetime import  datetime, timedelta
    import time
    
    start = time.time()
    
    in_twelve_hours_from_now = datetime.now() + timedelta(hours=12)
    print(format(in_twelve_hours_from_now, '{:%H:%M:%S}'))
    
    end = time.time()
    execution_time = end-start
    print(execution_time)

def timing3():
    from datetime import date, timedelta
    yesterday = date.today() - timedelta(days=1)
    return format(yesterday, '{:%yyyy:%mm:%dd}')
    
def timing4(): 
    from datetime import  datetime, timedelta
    in_twelve_hours_from_now = datetime.now() + timedelta(hours=12)
    return format(in_twelve_hours_from_now, '{:%H:%M:%S}')

print(timing3())
print(timing4())

import timeit
print(timeit.timeit('timing3()',setup="from __main__ import  timing3" ))
print(timeit.timeit('timing4()',setup="from __main__ import  timing4" ))


'''
2.13.
Exceptions
Read about exceptions from:
http://www.pythonforbeginners.com/error-handling/exception-
handling-inpython
1. Enhance the function you wrote which reads numbers (Strings 3.)
a. In case of a string input writing an error message 
   instead of raising an error
b. Raise an error in case one of the input numbers is > 100
c. Create a code which tries to read from the dictionary of 
   squares created 
'''
def dictionary_of_sq_enhanced():
    try:
        n = int(input())
    except:
        print('Error: only numbers, pls')
    if (n>100):
        raise Exception('Error: the number is bigger than 100', n)
    d = {i:i*i for i in range(1, n+1)}
    
    import ast
    with open("dictionaryfile.txt", "r") as data:
        dictionary = ast.literal_eval(data.read())
    print(dictionary)

'''
2.14.
Logger
Read about loggers from the example:
https://fangpenlin.com/posts/2012/08/26/good-logging-practice
-in-python/
Create a logger in any of your programs and log various messages
 to a fileusing a FileHandler, and to a the console using 
 StreamHandler
*Optional : try setting different levels (e.g. debug for 
console and info for file)and different formats and try 
different levels of logs in your code.
'''
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
hdlr = logging.FileHandler('myapp.log')
hdlr.setLevel(logging.DEBUG)
strhdlr = logging.StreamHandler()
strhdlr.setLevel(logging.ERROR)
formatter = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.addHandler(strhdlr)

try:
    n = int(input())
except:
    logger.error('Error: only numbers, pls')
if (n > 100):
    logger.error('''Error: the number is bigger than 100''')
    raise Exception('Exeption: the number is bigger than 100')
        
d = {i:i*i for i in range(1, n+1)}
file = open("dictionaryfile.txt", "w")
file.write(str(d))
file.close()
logger.info('the dictionary is made')
import ast
with open("dictionaryfile.txt", "r") as data:
    dictionary = ast.literal_eval(data.read())
logger.debug(dictionary)

'''
2.15
Regular expressions (re)
You can read about regex from the following sources:
Python documentation - https://docs.python.org/3/library/re.html
General links about RegEx - http://www.regular-expressions.info/
tutorial.html
And - https://www.icewarp.com/support/online_help/203030104.htm
(The last is more brief and practical)
Try to understand the difference between search and match (and 
compile),and how to match the strings exactly.
1. To get the hang of it, try to do a few of the the exercises in:
https://regexone.com/
2. To get a sense of regex in python, take a look at the first few
 exercises in: http://www.w3resource.com/python-exercises/re/
 3*. Optional: Write a regular expression for identifying email 
 addresses,find and compare to regular expression found online.
'''







































