import sys

def search(filename, expression):
    with open(f"{filename}", "r") as file:
        lines = file.readlines()
    line_number = 0
    for line in lines:
        line_number += 1
        if expression in line:
            return f"Found in {filename}\n{line.strip()} -> Line: {line_number}"

def main():
    filename = sys.argv[1]
    expression = sys.argv[2]
    print(search(filename, expression))


if __name__ == "__main__":
    main()