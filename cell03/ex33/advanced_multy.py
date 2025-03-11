row = 0
while row <= 10 :
    column = 0
    print(f"table de {row} :",end="")
    while column <= 10 :
        print(f"{row*column}",end=" ")
        column += 1
    row += 1
    print()
