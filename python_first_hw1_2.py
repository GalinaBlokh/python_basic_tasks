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
#Paul.menu_price()

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






























































