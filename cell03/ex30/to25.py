num = int(input("Enter the number less than 25 :")).__int__()
y = 25

if num > y :
    print("ERROR")

while num < 26 :
    for i in range(num,26):
        print(f"inside the loop, my varible is {num}")
        num += 1