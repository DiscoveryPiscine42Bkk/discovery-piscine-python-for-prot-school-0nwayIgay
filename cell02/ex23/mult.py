numone = int(input("input the first number"))
numtwo = int(input("input the second"))

result = int(numone*numtwo)
print(str(numone)+" "+"x"+" "+str(numtwo)+" "+"="+" "+str(result))

if result > 0:
    print("The result is positive")

elif result < 0:
    print("The result is negative")

elif result == 0:
    print("The result is positive and negative")