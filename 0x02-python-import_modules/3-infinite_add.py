#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for argv in sys.argv:
        if argv != sys.argv[0]:
            result += int(arg)
        print (result)
