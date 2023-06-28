


# how does while loop works
# while loop is a conditional loop
# it will keep running until the condition is true
# once the condition is false, it will stop running

# i = 0
# while i < 10:
#     print(i < 10)
#     i += 1
# print("--------------------")

# password = "pass123"
# user_input = ""
# counter = 0

# while user_input != password and counter < 3:
#     # if counter == 3:
#     #     print("You have reached maximum number of tries")
#     #     break
#     user_input = input("Enter your password: ")
#     counter += 1

# # print("You are logged in")


while True:
    name = input("Enter your name: ")
    if name != "hara":
        continue
    else:
        break
print("You are logged in")