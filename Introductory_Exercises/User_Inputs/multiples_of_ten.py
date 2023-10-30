multiples = input("Say me a number and I will verify if it is a multiple of 10: ")
multiples = int(multiples)

if multiples % 10 == 0:
    print("The number " + str(multiples) + " is a multiple of 10.")
else:
    print("The number " + str(multiples) + " isn't a multiple of 10.")
    