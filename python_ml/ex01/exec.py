import sys

args_num = len(sys.argv)

if (args_num == 1):
    print("Please provide one or more arguments.")
    sys.exit(1)

input = ' '.join(sys.argv)
print(f"You provided {str(args_num)} arguments: '{input}'")
