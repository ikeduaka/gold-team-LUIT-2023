def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()
############################
def hello():
    print("Hello world!")

hello()
#################################

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

####################################

def print_double(x):
   print(2 * x)

print_double(3)
#################################

password = input()
repeat = input()

def validate(text1, text2):
	if text1 == text2:
		print("Correct")
	
	else:
		print("Wrong")

validate(password, repeat)
########################################

