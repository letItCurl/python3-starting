# multiple lines text >3
text = """ gdgwsjhdbg
sfhdhksdfhsdfh
fdhsihsodifhsoidfkhj
dfshfihldfhbf """

# input from shell
name = input("What is your name?: ")
age = input("What is your age?: ") # return int !
city = input("From where city are you from?: ")
love = input("What do you love?: ")

# hello world !
string = "you are {}, your age is {}, you live in {} and you love {}".format(name,age,city,love)
print(string)

# yes like ruby !
print("="*20)

# string concatenetion
A = "part one"
B = "part two"
C = A + B
print(C)



# int to str | str to int
print('1' + str(21))
print(21 + int("1"))

# format
D = "{0} , {1} and again the first one {0}, then {2}".format(A,B,name)
print(D)

# yes like ruby !
print("="*20)


