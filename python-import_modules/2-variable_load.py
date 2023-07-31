def main():
    with open("variable_load_2.py") as f:
        code = f.read()
        exec(code, globals())
        print(a)
    
if __name__ == "__main__":
    main()