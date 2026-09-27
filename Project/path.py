from pathlib import Path

# print(Path.cwd()) # Current working directory - cwd

# for p in Path().iterdir():
#     print(p)

my_dir = Path("Directory_1")
new_file = my_dir / "dfile.py" # or my_dir.joinPath("dfile.txt")
# Creates an empty Python file
new_file.touch()
new_file.write_text("print(\"Hello, World\")")

# .stem - only name
# .suffix - for filetype (.txt, .py ...)
# .exists() return T/F 
# .parent
# .absolute() / .resolve()

# print(my_dir.parent)
# print(new_file.parent.parent)

p = Path(__file__).resolve() # current file
# print(p)

# Option 1: String with multiple levels
p1 = Path("../../").resolve()
# Option 2: Using pathlib's .parent property (cleaner and safer!)
p2 = Path(".").resolve().parent.parent 
# print(p1)
# print(p2)

p = Path("~/.vscode").expanduser().resolve()
print(p)

for f in p.iterdir():
    print(f)