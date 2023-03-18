import sys

args_num = len(sys.argv)

if (args_num == 1 or args_num > 2):
    print("Please provide one argument.")
    sys.exit(1)

input = sys.argv[1]

try:
    input_int = int(sys.argv[1])
    input_float = float(sys.argv[1])

    if (input_int != input_float):
        raise Exception()
except:
    print("Please insert an integer number.")
    sys.exit(1)

print(f"Your inputted number ({input}) is ", end="")

if (input_int == 0):
    print("zero.")
elif (input_int % 2 == 0):
    print("even.")
else:
    print("odd.")
