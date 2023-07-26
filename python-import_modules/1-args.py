#!/usr/bin/python3
from sys import argv


def main():
    print("{} argument".format(len(argv)), end="")
    if len(argv) != 1:
        print("s", end="")
        if len(argv) == 0:
            print(".")
        else:
            print(":")

    for i in range(1, len(argv)+1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
