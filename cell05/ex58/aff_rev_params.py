import sys

if len(sys.argv) < 3 :
    print("none")

else :
    for h in list(reversed(sys.argv[1:])):
        print(h)