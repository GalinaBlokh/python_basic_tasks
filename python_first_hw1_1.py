#1.
print("Hello world")

# 2.
message = "Level Two"
print(message)

# 3.
print(type(message))

# 4.
a = 123
b = 654
c = a + b
print(c)

# 6.
a = 100
print(a)
c = 50
print(c)

d = 10 + a - c
print(d)

# 7.
greeting = 'Hi '
name = 'Gala'
message = greeting + name
print(message)

# 8.
age = 37
#print(name + ' is ' + age + ' years old')

# 9.
print(name + ' is ' + str(age) + ' years old')

age = str(37)
print(name + ' is ' + age + ' years old')

# 10.
bobs_age = 15
your_age = 37
print(bobs_age == your_age)

# 11.
bob_is_older = bobs_age > your_age
print(bob_is_older)

# 12.
money = 500
phone_cost = 240
tablet_cost = 200

total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost

if can_afford_both:
    message = "You have enough money for both"
else:
    message = "You can't afford both devices"
print(message)

money = 500
phone_cost = 240
tablet_cost = 260

total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost

if can_afford_both:
    message = "You have enough money for both"
else:
    message = "You can't afford both devices"
print(message)

raspberry_pi = 25
pies = 3 * raspberry_pi

total_cost = total_cost + pies

if total_cost <= money:
    message = "You have enough money for 3 raspberry pies as well"
else:
    message = "You can't afford 3 raspberry pies"
print(message)

# 13.
colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print('Black' in colours)

colours.append('Black')
colours.append('White')
print('Black' in colours)

more_colours = ['Gray', 'Navy', 'Pink']
colours.extend(more_colours)
print(colours)

# 14.
primary_colours = ['Red', 'Blue', 'Yellow']
secondary_colours = ['Purple', 'Orange', 'Green']

main_colours = primary_colours + secondary_colours
print(main_colours)

# 15.
print(len(primary_colours))
print(len(secondary_colours))
print(len(main_colours))

all_colours = colours + main_colours
print(len(all_colours))

# 16.
even_numbers = [2, 4, 6, 8, 10, 12]
multiples_of_three = [3, 6, 9, 12]

numbers = even_numbers + multiples_of_three
print(numbers, len(numbers))
numbers_set = set(numbers)
print(numbers_set, len(numbers_set))
colour_set = set(all_colours)
print(colour_set, len(colour_set))

# 17.
my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']
for student in my_class:
    print(student)
my_class.append('Gala',)
my_class.append('Lea')
my_class.append('Rakhel')
my_class.append('Denit')
my_class.append('Sharon')

count = 0
for student in my_class:
    count += 1
    print(str(count) + ' ' + student)
    
# 18.
full_name = 'Dominic Adrian Smith'

first_letter = full_name[0]
last_letter = full_name[19]
first_three = full_name[:3]  # [0:3 also works]
last_three = full_name[-3:]  # [17:] and [17:20] also work
middle = full_name[8:14]
print(first_letter + first_three + last_three + last_letter)
print(first_letter + last_letter + first_three + last_three)
print(full_name[4] + full_name[8] + full_name[19] + full_name[8] 
      + full_name[10:13] + full_name[19])

# 19.
my_sentence = "Hello, my name is Fred"
parts = my_sentence.split(',')
print(parts)
print(type(parts))

my_long_sentence = "This is a very very very very very very long sentence"
parts2 = my_long_sentence.split(' ')
print(len(parts2))

# 20.
person = ('Bobby', 26)
print(person[0] + ' is ' + str(person[1]) + ' years old')

students = [
    ('Dave', 12),
    ('Sophia', 13),
    ('Sam', 12),
    ('Kate', 11),
    ('Daniel', 10)
]
for student in students:
    print(student[0] + ' ' + str(student[1]))

for student in students:
    print(student)

# 21.
#  a list of students with  (name, age, favourite subject and sport)
students = [
       ('David', 17, 'physics', 'surfing'),
       ('Sofia', 16, 'mathematics', 'dances'),
       ('Sam', 17, 'history', 'football'),
       ('Kate', 18, 'mathematics', 'surfing'),
       ('Daniel', 16, 'programming', 'computer games'),
       ('Olga', 18, 'programming', 'computer games')
        ]
for student in students:
    print(student)
    
for student in students:
    if student[1] > 16 and student[1] < 18:
        print(student)
    
for student in students:
    if student[1] > 17:
        print(student)

# 22.
addresses = {
    'Lauren': '0161 5673 890',
    'Amy': '0115 8901 165',
    'Daniel': '0114 2290 542',
    'Emergency': '999'
}
print(addresses['Amy'])
print('David' in addresses)
print('Daniel' in addresses)
print('999' in addresses)
print('999' in addresses.values())
print(999 in addresses.values())

addresses['Amy'] = '0115 236 359'
print(addresses['Amy'])

del addresses['Daniel']
print( 'Daniel' in addresses)

for name in addresses:
    print(name, addresses[name])

# 23.
sum = 0
for num in range(1001):
    sum += num
print(sum)














































