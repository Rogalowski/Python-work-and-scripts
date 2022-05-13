from pathlib import Path
import shutil

# with open('test.txt') as f:
#     s = f.read()
s = "asdasdsa"
with open('test2.txt', "w") as f:
    f.write(s)

# f = open('test.txt')
# try:
#     s = f.read()
# finally:
#     f.close()

# https://docs.python.org/3/library/pathlib.html
a = Path('/var/lib') / "logs/asdf/.." / Path("test.log")
print(a.resolve())
print(a.is_file())
for f in Path('.').iterdir():
    print(f)
#.is_dir()
#.is_file()

Path('test2.txt').unlink()

k = Path('testowy-katalog')
k.mkdir(exist_ok=True)
(k / "test1.txt").touch()
(k / "test2.txt").touch()
(k / "test3.txt").touch()


shutil.rmtree(k)
#.copytree(k)
