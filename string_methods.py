a = "hello".count('l')
print(a)

x = "Happy Birthday"
print(x.lower()) # not descrutive
print(x.upper()) # not descrutive
print(x.capitalize()) # not descrutive
print(x.title()) # not descrutive

print(x.islower()) # not descrutive
print(x.isupper()) # not descrutive
print(x.isalpha()) # not descrutive
print(x.istitle()) # not descrutive
print(x.isdigit()) # not descrutive
print(x.isalnum()) # not descrutive

print(x.index("Birthday"))
# print(x.index("gfsdg")) # will crash
print(x.find("Birthday"))
print(x.find("gfsdg"))

y = "     000000sdfbvdsfbsdf0bfd0bsdfb0f0bsdfbfhsdfhbdf00000000000000     "
print(y.strip('0'))
print(y.lstrip('0'))
print(y.rstrip('0'))
print(y.strip())