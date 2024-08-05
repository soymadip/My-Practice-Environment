# name = "Soumadip"


# print(len(name)) # In range, counting starts from 1

# print(name[0:7:2])
# #     [ start: End: Jump index]

# print(name[-1])


# String Methods

# range starts from 1 to ...
# index starts from 0
# string slicing starts from o to range -1
# negative index starts from -1 to rahge
# So range and negative is same but opposite

# import datetime

# name = input("Enter your name: ")
# date = datetime.datetime.now()

# letter = f'''
# Dear {name},
# You are selected!
# {date}
# '''

# print(letter)


# def detect_double_space(string):
#     if string.find("  ") != -1:
#         print(string.replace("  ", " "))
#         print(string.find("  "))
#     elif(string.find("  ") == -1):
#         print("Bhooya")
#         print(string.find("  "))
#     else:
#         return

# detect_double_space(input("Enter your name\nDouble spaces will be replaced with one.\n=> "))


# print("i am a boy who is \"Terrificly terrified\"")
# print("i am a boy\\google employee.")



# friends = [ "alpple", "google", 5, ["google", 48]]

# print(friends[3])

# friends[3] = 50000

# print(friends)

# friends2 = [10, 11, 2000 ]
# friends2.sort(reverse=True)
# print(friends2)

# print(friends.index("alpple"))

# input("I am google employee:")

# print("google.com")


# for i in range(10):
    # print(i)




my_string = "Soumadip Das  "

print(my_string.lower())
print(my_string.upper())
print(my_string.split("-")[0])
print(my_string.strip())
print(my_string.replace("-", " "))
print(my_string.find("Das"))
print(my_string.isalpha())
print(my_string.isdigit())
print(my_string.startswith("Hello"))
print(my_string.isalnum())
print(my_string.endswith(" "))

print(my_string.count("a"))
