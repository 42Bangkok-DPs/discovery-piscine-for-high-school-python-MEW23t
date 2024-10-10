#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    parameter = sys.argv[1]
    user = input("Enter a word: ")
    if user == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()
