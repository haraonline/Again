import os

# this is a comment
print("hallo again ...")
print('hello again ...')
print('das ist ein "Haus"...')
print("das ist ein 'Haus'...")

age = 32
print(age)
age = 29
print(age)

a = b = c = 1
print(a)
print(b)
print(c)
a = b = c = 3
print(a)
print(b)
print(c)

# variable names are case-sensitive
age = 5
Age = 10
print(age)
print(Age)

# datatypes in python
int1 = 5
float1 = 13.345
float2 = 13e3
float3 = 2.
float4 = .659
float5_inf1 = 10e999
float5_inf2 = -10e999

name = "hara"
print(name)
name = 45
print(name)

# input function
# result = input(__prompt := "bitte geben Sie hier etwas: ")
# print(result)

# clear console in python
os.system("cls")

# value1 = int(input("enter the first number : ..."))
# value2 = float(input("enter the second number: ..."))
# addition
# print(value1 + value2)

# a mixed list
mixedList = [1, 2, 3, 4, 5, "hara", 3.14, True]
print(mixedList)

# list slicing
print(mixedList[5])
print(mixedList[0:5])
print(mixedList[0:5:2])
print(mixedList[0:5:3])
print(mixedList[-3])
mixedList[0] = "malena"
print(mixedList[:6])
print(mixedList[3:])


# list methods

print(len(mixedList))

# append (add an element to the end of the list)
mixedList.append("jennifer")
print(mixedList)

# insert (add an element at the given index)
mixedList.insert(2, "Anna")
print(mixedList)

# remove (remove the first occurrence of an element)
mixedList.remove("Anna")
print(mixedList)

# pop (remove the last element)
mixedList.pop()
print(mixedList)

# del (remove the element at the given index)
del mixedList[3]
print(mixedList)

# clear (remove all elements)
mixedList.clear()
print(mixedList)

# copy (shallow copy)
mixedList = [1, 2, 3, 4, 5, "hara", 3.14, True]
mixedList2 = mixedList.copy()

# count (count the number of occurrences of an element)
print(mixedList.count("hara"))

# extend
mixedList.extend(mixedList2)
print(mixedList)

# index
print(mixedList.index(3))

# reverse
mixedList.reverse()
print(mixedList)

# sort
mixedList.sort()
print(mixedList)

# list comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [i * 2 for i in list1]
print(list2)

# nested list
nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nestedList[0][1])















