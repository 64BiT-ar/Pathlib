from pathlib import Path

# dotfiles = Path.cwd().resolve()
# # print(dotfiles)

# for p in dotfiles.glob("*dfile*"): # only search main directories
#     print(p)

# # for main and sub directories
# for p in dotfiles.rglob("*dfile*"):
#     with p.open() as f:
#         print(f.read())

# -------------------

p = Path("TempDir").resolve()
p.mkdir(exist_ok=False)
p.rmdir() # Only remove empty Dir
print(p)