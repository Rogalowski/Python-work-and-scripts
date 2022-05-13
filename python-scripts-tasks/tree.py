#!/usr/bin/env python
from pathlib import Path
import argparse

def print_dir(dir, options, indent=''):
    for f in dir.iterdir():
        if f.is_dir():
            print(f"{indent}- [{f}]")
            print_dir(f, options, indent+' '*options.width)
        else:
            print(f"{indent}- {f}")

def main():
    parser = argparse.ArgumentParser(description="Rysuje drzewo plików")
    parser.add_argument('-w', '--width', type=int, default=2)
    parser.add_argument('--flat', action='store_const', dest='width', const=0)
    args = parser.parse_args()

    print_dir(Path('.'), args)


if __name__ == "__main__":
    main()