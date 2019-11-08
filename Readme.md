# Numbers = Int, Float

`print(type((1))`

# String
---
## Indexing
- mystring[index]

## Slicing
- mystring([2:1])

## Basic methods
- mystring.upper()

## Print formatting
- "Inserting another string here: {}".format("INSERT FORMAT")
- "Item One: {y} Item Two: {x}".format(x="dog", y="cat")

# List (Array)
---
mylist = [1,2,3]
mylist = len([1,2,3])

## Indexing
- mylist[-1] - from behind

## Slicing
- mylist[1:]

## Basic methods
mylist.append(yourList)
mylist.extend(yourList)
mylist.pop()
mylist.reverse() - self assignment
mylist.sort() - self assignment

# Dictionary (Object)
---
my_stuff = {"key1": "value"}

# Booleans
- True / False / 0 / 1

# Tuples - immutable sequences
t = (1,2,3)

# Sets - unique value
x = set()
x.add(1)
x.add(2)

# Control Flow
- 1 == 1 True
- 1 == '2' False
- 1 !== 2 True
- (1 > 2) and (2 < 3)
- (1 > 2) or (2 < 3)

## If statment
```
if 1  > 2:
  print("2")
elif 3 == 3:
  print("cool")
else:
  print("3")
```

## For loops
```
seq = [1,2,3,4,5,6]

for item in seq:
  print(item)
```

```
d = {"Sam": 1, "Frank": 2, "Dan": 3}

for key in d:
  print(key)
  print(d[key])
```

```
myparis = [(1,2),(3,4),(5,6)]

for (tup1, tup2) in mypairs:
  print(tup1)
  print(tup2)

output: 1 2 3 4 5 6
```

```
i = 1

while i < 5:
  print("i is: {}".format(i))
  i = i + 1
```

```
range(5) = range(0,5)
list(range(0,5)) = [0,1,2,3,4]
list(range(0, 20, 2)) = [0,2,4,6,8,10,12,14,16,18,20]

for item in range(10):
  print(item)
```

```
x = [1,2,3,4]
out = [num**2 for num in x]
```

# Functions
```
def my_func(param='default'):
  """
  THIS IS THE DOCSTRING
  """"
  print("my first python function! {}".format(param))

my_func()
```

# Filter
```
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
  return num % 2 == 0

evens = filter(even_bool, mylist)
print(list(evens))
```

# Lambda Expression
```
mylist = [1,2,3,4,5,6,7,8]

evens = filter(lambda num:num % 2 == 0, mylist)
print(list(evens))
```

# Check is something inside the list
`print ('x' in [1,2,3,'x'])` = True

# Python scope
- Follow LEGB Rule:
  - Local
  - Enclosing Function locals
  - Global
  - Built-in

## LOCAL
lambda x: x**2

## Enclosing function locals
name = 'This is a global name!'

def greet():
  name = "sammy"

  def hello():
    print("hello"+name)

  hello()

greet() << sammy

## Global - global can be modified
x = 50

def func():
  global x
  x = 1000

func() << x is now 1000

## Built in - example like len()

# Class
```
class Animal():

  // class object attribute
  count = 50

  def __init__(self,breed):
    self.breed = breed

  def random_func(self):
    return self.breed

myAnimal = Animal(breed = "Lab")
print myAnimal.breed
```

# Inheritance
```
class Animal():

  def __init__(self):
    print("ANIMAL CREATED")

  def whoAmI(self):
    print("ANIMAL")

  def eat(self):
    print("EATING")

mya = Animal()
mya.whoAmI()

class Dog(Animal):

  def __init__(self):
    Animal.__init__(self)
    print("DOG CREATED")

  def __str__(self):
    return "basical the toString method"

  def __len__(self):
    return 10

  def __del__(self):
    print("Dog destroyed something")

myDog = Dog()
myDog.eat()
print(myDog) = __str__
print(len(myDog)) = __len__
del myDog
```

# Error Handling
try:
  f = open('simple.txt', 'r') // w instead of r
  f.write('Test write into txt')
except IOError:
  print("ERROR: COULD NOT FIND THE FILE OR READ DATA!")
except:
  print("GENERAL EXCEPTION")
finally: or else:
  print("SUCCESS")
  f.close()

# Regular Expression
```
import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, not ther other!'

for pattern in patterns:
  print("I'm searching for" + pattern)

  if re.search(pattern, text):
    print("match")
  else:
    print("not match")

match = re.search('term1', text)

print(match.start()) // first index of match value


split_term = '@'
email = 'user@gmail.com'

print(re.split(split_term,email))


re.findall('match', 'test phrase match in the match middle') = return a list of matches


def multi_re_find(patterns, phrase):

  for pat in patterns:
    print("Searching for pattenr {}".format(pat))
    print(re.findall(pat.phrase))
    print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['sd*'] // 0 or more d
test_patterns = ['sd?'] // 0 or 1 d
test_patterns = ['sd+'] // 1 or more d
test_patterns = ['sd{3}'] // 3 d
test_patterns = ['sd{1,3}'] // 1 - 3 d
test_patterns = ['s[sd]+'] // s follow by 1 or more s or 1 or more d 

multi_re_find(test_patterns, test_phrase)


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

test_patterns = ['[^!.?]+'] << search for ! . ?, ^ is remove all the characters
test_patterns = ['[a-z]+'] << get sequence of all lowercase
test_patterns = ['[A-Z]+'] << get sequence of all uppercase

test_patterns = [r'\d+'] << sequence of digit
test_patterns = [r'\D+'] << sequence of non-digit
test_patterns = [r'\s+'] << sequence of white-space
test_patterns = [r'\S+'] << sequence of non-white-space
test_patterns = [r'\w+'] << sequence of digit and alphabet
test_patterns = [r'\W+'] << sequence of non-digit and non-alphabet


multi_re_find(test_patterns, test_phrase)
``` 

# Decorator
```
s = "GLOBAL VARIABLE"

def func(s):
  mylocal = 10
  print(locals()) // get local variable
  print(globals()['s']) // get global s

func()

print(func())

def hello(name="Jose"):
  return "hello"+name

print(hello())
```

```
def new_decorator(func):
  xxx

@new_decorator // equivalent to func_needs_decorator = new_decorator
def func_needs_decorator():
  print("SOMETHING")

func_needs_decorator()
```
