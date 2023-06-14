#!/usr/bin/python3
import sys
def main():
    num_args = len(sys.argv)
    print(f"{num_args} arguments:")
    if num_args == 0:
        print(".")
        return
    for i in range(1, num_args + 1):
        print(i, ":", sys.argv[i - 1])
if __name__ == "__main__":
    main()
