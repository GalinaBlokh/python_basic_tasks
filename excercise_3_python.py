## Very simple exercises
'''
1. Define a function `max()` that takes two numbers as arguments 
and returns the largest of them. Use the if-then-else construct 
available in Python. (It is true that Python has the `max()`
function built in, but writing it yourself is nevertheless a good
 exercise ).
'''
def maximums(a, b):
    if a > b :
        return a
    else:
        return b
    
'''
2. Define a function `max_of_three()` that takes three numbers as 
arguments and returns the largest of them.
'''
def max_of_three(a, b, c):
    maximum = maximums(maximums(a, b), c)
    return maximum

'''
3. Define a function that computes the length of a given list or 
string. ( It is true that Python has the `len()` function built in,
 but writing it yourself is nevertheless a good exercise ).
'''
def length(list_or_str):
    count = 0
    for i in list_or_str:
        count += 1
    return count

'''
4. Write a function that takes a character ( i.e. a string of
 length 1 ) and returns `True` if it is a vowel, `False` otherwise.
'''
def is_vowel(char):
    vowel = ('a', 'e', 'i', 'o', 'u')
    if char not in vowel:
        return False
    return True

'''
5. Write a function `translate()` that will translate a text into
 "rövarspråket" (Swedish for "robber's language"). That is, double
 every consonant and place an occurrence of "o" in between. For
example, `translate("this is fun")` should return the string 
`"tothohisos isos fofunon".`
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

'''
6. Define a function `sum()` and a function `multiply()` that sums
 and multiplies (respectively) all the numbers in a list of 
 numbers. For example, `sum([1, 2, 3, 4])` should return `10`,
 and `multiply([1, 2, 3, 4])` should return `24`.
'''
def sum_retrospective(lst):
    b = 0
    for a in lst:
        b += a
    return b  

def multiply_retrospective(lst):
    b = 1
    for a in lst:
        b *= a
    return b  
'''
7. Define a function `reverse()` that computes the reversal of a 
string. For example, `reverse( "I am testing" )` should return the
 string `"gnitset ma I"`.
'''
def reverce_function() :
    s = input() 
    c = s[::-1]
    return c

'''
8. Define a function `is_palindrome()` that recognizes palindromes
 (i.e. words that look the same written backwards). For example,
 `is_palindrome( "radar" )` should return `True`.
 '''
def is_it_palindrome():
   s = input() 
   i = 0
   j = len(s)-1
   is_palindrome = True
   while i < j:
       if s[i] != s[j]:
           is_palindrome = False
           break
       i+=1
       j-=1
       if is_palindrome:
           print('yes')
       else:
           print('no')
        
'''
9. Write a function `is_member()` that takes a value ( i.e. a 
number, string, etc ) `x` and a list of values `a`, and returns 
True if `x` is a member of `a`, `False` otherwise. (Note that this
 is exactly what the in operator does, but for the sake of the
 exercise you should pretend Python did not have this operator).
'''
def is_member(x, lst):
    for a in lst:
        if a == x:
            return True
        else:
            return False
    

'''
10. Define a function `overlapping()` that takes two lists and 
returns `True` if they have at least one member in common, 
`False` otherwise. You may use your `is_member()` function, 
or the in operator, but for the sake of the exercise, you should 
(also) write it using two nested for-loops.
'''
def overlapping(list1, list2):
    res = False
    for i in list1:
        for j in list2:
            if j == i:
                res = True
    return res

'''
11. Define a function `generate_n_chars()` that takes an integer 
`n` and a character `c` and returns a string, `n` characters long,
 consisting only of c:s. For example, `generate_n_chars(5,"x" )`
 should return the string `"xxxxx"`. (Python is unusual in that
 you can actually write an expression `5 * "x"` that will evaluate
 to `"xxxxx"`. For the sake of the exercise you should ignore that
 the problem can be solved in this manner ).
 '''
def generate_n_chars(numbers, letters):
    s = ''
    for n in range(numbers):
       s += letters
    return s
 
'''
12. Define a procedure `histogram()` that takes a list of integers
 and prints a histogram to the screen. For example,
 `histogram( [ 4, 9, 7 ] )` should print the following:
```
****
*********
*******
```
'''
def histogram(lst):
    s = '*'
    for n in (lst):
        print(s * n)

'''
13. The function `max()` from exercise 1) and the function 
    `max_of_three()` from exercise 2) will only work for two and 
    three numbers, respectively. But suppose we have a much 
    larger number of numbers, or suppose we cannot tell in advance 
    how many they are? Write a function `` that takes
    a list of numbers and returns the largest one.
'''
def max_in_list(lst):
    sorted_list = sorted(lst)
    return sorted_list[-1]
    

'''
14. Write a program that maps a list of words into a list of 
integers representing the lengths of the corresponding words.
'''
def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
'''
15. Write a function `find_longest_word()` that takes a list of 
words and returns the length of the longest one.
'''
def find_longest_word(words):
    longest_word = max(words, key = len)
    return len(longest_word)

'''
16. Write a function `filter_long_words()` that takes a list of 
words and an integer `n` and returns the list of words that are 
longer than `n`.
'''
def filter_long_words(words, n):
    words_more_than_n= []
    for i in range(len(words)):
      if len(words[i]) > n:
          words_more_than_n.append(words[i])
    return words_more_than_n

'''
17. Write a version of a palindrome recognizer that also accepts 
phrase palindromes such as "Go hang a salami I'm a lasagna hog.", 
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan,
 Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic 
 sonatas", "I roamed under it as a tired nude Maori", "Rise to
 vote sir", or the exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored.
'''
import re
def is_palindrome2(frase):
    words = [] 
    frase = re.sub('[^a-zA-Z]', '', frase).lower()
    for s in frase:
        words.insert(0, s)
    if frase == ''.join(words):
        return True
    else:
        return False

'''
18. A pangram is a sentence that contains all the letters of the
 English alphabet at least once, for example: "The quick brown fox
 jumps over the lazy dog". Your task here is to write a function
to check a sentence to see if it is a pangram or not.
'''
def pangram_check(sentence):
    alphabets=['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    words = re.sub('[^a-zA-Z]', '', sentence).lower()
    i = 0
    for letter in alphabets:
        if letter in words:
            i += 1
    if i == len(alphabets):
        return  True
    else:
        return False

'''
19. "99 Bottles of Beer" is a traditional song in the United States
 and Canada. It is popular to sing on long trips, as it has a very
 repetitive format which is easy to memorize, and can take a long
 time to sing. The song's simple lyrics are as follows:
```99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.```
The same verse is repeated, each time with one fewer bottle. 
The song is completed when the singer or singers reach zero.
 Your task here is write a Python program capable of generating all
the verses of the song.
'''
def bottles_of_bear(bottles):
    for i in range(99,0,-1):
        print(str(i)+" bottles of beer on the wall, "+str(i) +" bottles of beer.")
        print("Take one down, pass it around, "+str(i-1) +" bottles of beer on the wall.")
        print (" ")   
        
'''
20. Represent a small bilingual lexicon as a Python dictionary in
 the following fashion
```
{ "merry":"god", "christmas":"jul", "and":"och", "happy":gott",
 "new":"nytt", "year":"år" }
```
and use it to translate your Christmas cards from English into
 Swedish. That is, write a function `translate()` that takes a list
 of English words and returns a list of Swedish words.
 '''
def translate(eng_words):
    dictionary = { "merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
 "new":"nytt", "year":"år" }
    swedish =[]
    for word in eng_words.lower().split():
        if word in dictionary:
            swedish.append(dictionary[word])
    return ''.join(swedish)
 
'''
21. Write a function `char_freq()` that takes a string and builds
 a frequency listing of the characters contained in it. Represent
 the frequency listing as a Python dictionary. Try it with 
 something like `char_freq("abbabcbdbabdbdbabababcbcbab")`.
 '''
def char_freq(word):
    dictionary={}
    for i in (range(len(word))):
        if (word[i] in dictionary):
            dictionary[word[i]]=int(dictionary.get(word[i]))+1
        else:
            dictionary[word[i]]=1     
    return dictionary
 
'''
22. In cryptography, a Caesar cipher is a very simple encryption 
techniques in which each letter in the plain text is replaced by a
 letter some fixed number of positions down the alphabet. For
example, with a shift of 3, A would be replaced by D, B would 
become E, and so on. The method is named after Julius Caesar, 
who used it to communicate with his generals. `ROT-13
("rotate by 13 places")` is a widely used example of a Caesar 
cipher where the shift is 13. In Python, the key for ROT-13 may
 be represented by means of the following dictionary:
```
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':
    't', 'h':'u','i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z',
    'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g',
    'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N',
    'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U',
    'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B',
    'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
```
Your task in this exercise is to implement an encoder/decoder of 
ROT-13. Once you're done, you will be able to read the following
 secret message:
```
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
```
Note that since English has 26 characters, your ROT-13 program will
 be able to both encode and decode texts written in English.
 '''
def decoder_encoder(frase):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    newString = ""
    for word in (re.findall('[a-zA-Z0-9?!]+', frase)):
        for j in range(len(word)):
            if word[j] in key:
                newString = newString + key[word[j]]
            else:
                newString = newString+word[j]
        newString = newString+" "
    return newString 
 
'''
23. Define a simple "spelling correction" function `correct()` 
that takes a string and sees to it that 
1) two or more occurrences of the space character is compressed 
    into one, and 
2) inserts an extra space after a period if the period is directly
    followed by a letter. E.g. `correct("This is very funny and
    cool.Indeed!")` should return "This is very funny and cool.
    Indeed!" Tip: Use regular expressions!
'''

def correction(frase):
    correction1 = re.sub('\ +',' ',frase)
    correction2 = re.sub('\.','. ',correction1)
    return correction2
 
