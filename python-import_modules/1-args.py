import sys

def main():
    args = sys.argv[1:]  # Exclude the script name from the arguments list
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Print each argument and its position
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
