import sys

if len(sys.argv) == 2:
    inputstring = sys.argv[1]
    count = inputstring.count('z')
    if count > 0 :
        for x in range(count):
            print("z", end='')
    elif count < 1:
        for x in range(count):
            print("none")
        
else :
    print("none")