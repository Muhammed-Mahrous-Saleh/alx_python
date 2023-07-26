#!/usr/bin/python3
from sys import argv


def main():
    print("{} argument".format(len(argv)-1), end="")
    if len(argv) != 2:
        print("s", end="")
        if len(argv) == 1:
            print(".")
    if len(argv) != 1:
            print(":")

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
