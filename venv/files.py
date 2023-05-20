from pathlib import Path

path=Path("mall")
#path.mkdir()
#path.rmdir()
print(path.exists())
#path.rmdir()
for i in path.glob('*'):
    print(i)
for j in path.glob('*.*'):
    print(j)
for pyth in path.glob('*.py'):
    print(pyth)
for xlc in path.glob('*.xlc'):
    print(xlc)

