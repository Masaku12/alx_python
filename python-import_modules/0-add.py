def add(a, b):
    return (a + b)

def main():
    from add_0 import add
    a = 1
    b = 2
    
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()