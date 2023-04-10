first_name = "Monty"
last_name = "Python"

print(first_name+" "+last_name)
############################################### string

first_name = "John"
surname = "Doe"

print("My first name is {}. My family name is {}".format(first_name, surname))

################################################# Strings
firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")

############################################# Number Integer
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

################################################# Dictionary
user = {"first_name":"Ada"}  ###
print(user)

user = {"first_name":"Ada"}   #### read value with key
print(user["first_name"])

user["family_name"] = "Byron"  ### add key-value
print(user)

user["family_name"] = "Lovelace" #### modify a value
print(user)

del user["family_name"]  ### delete key-value pair
print(user)

################################################ list
fruit = ["apples","oranges","bananas"]  ### creating
print(fruit[1])
