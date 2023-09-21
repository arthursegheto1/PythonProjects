names = ['Arthur','Matheus','Felipe','Pedro','João']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print("The three first names are: ")
for name in names[:3]:
    print(name.title())

print("\nThe three names in the middle of the list are: ")
for name in names[1:4]:
    print(name.title())

print("\nThe three last names are: ")
for name in names[-3:]:
    print(name.title())