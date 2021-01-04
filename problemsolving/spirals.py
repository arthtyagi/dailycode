import sys
arg1 = str(sys.argv[1])
arg2 = int(sys.argv[2])


def process(arg1, arg2):
    newstring = ''
    for i in range(arg2-1):
        newstring = arg1[1:]+arg1[0]
        print(newstring)
        arg1 = newstring


if ((int(arg2) > 1) and (int(arg2) < 100)):
    print(arg1)
    process(arg1, arg2)
else:
    sys.exit()
