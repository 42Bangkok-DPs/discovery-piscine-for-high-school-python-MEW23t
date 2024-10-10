#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return
    try:
        num1 = int(sys.argv[1]) 
        num2 = int(sys.argv[2])
    except ValueError:
        print("none")
        return

    number = list(range(num1, num2 + 1))
    print(number)

if __name__ == "__main__":
    main()
