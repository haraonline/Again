
# lists are mutable (elements can be changed i.e, added, removed, or replaced)
# tuples are immutable (elements cannot be changed i.e, added, removed, or replaced)
# lists are defined using square brackets []
# tuples are defined using parentheses ()
# lists are slower than tuples
# the performance is negligible for small lists and tuples
# importance difference is mutability
# if you wish to store just one element in parentheses, you need a trailing comma



# example of a list
list_of_numbers = [1, 2, 3, 4, 5]
print(list_of_numbers[2])
print(list_of_numbers)


# example of a tuple
tuple_of_numbers = (1, 2, 3, 4, 5)
print(tuple_of_numbers[3])
print(tuple_of_numbers)

# example of a tuple with one element
tuple_of_numbers = (1,)

# unpacking a tuple
person = ("John", "Doe", 53)
print(person)
first_name, last_name, age = person # unpacking a tuple
print(first_name)

# or normally
person = ("John", "Doe", 53)
first_name = person[0]
last_name = person[1]
age = person[2]


# return a tuple from a function
def get_person():
    name = "John"
    age = 53
    country = "USA"
    return name, age, country

person = get_person()
print(person)

# arbitratory number arguments as a tuple
def multiply(*args):
    x = 1
    for arg in args:
        x *= arg
    return x

print(multiply(2, 4, 6))

print(multiply()) # returns 1 and is wrong, rewritten below

def multiply2(num1, num2, *args):
    x = num1 * num2
    for arg in args:
        x *= arg
    return x


# print options
print("Hello", "World", sep=" --- ", end=" *** ")
print("Hello", "again", sep=" --- ", end=" >>> ")
print("bye") # default end is \n
print("see you later")
print("this", "is", "a", "test", sep=" ")


def print_name(first_name, last_name):
    global title    
    print("Hello", title, first_name, last_name)        

title = "Dr"
print_name("John", "Doe")
