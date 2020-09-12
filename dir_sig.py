#!/usr/bin/env python3.7

from pathlib import Path
import hashlib

dir_dict={}

def recurse_dir(p: Path):
    global dir_dict
    for i in p.iterdir():
        if i.is_file():
            h = hashlib.new('md5')
            h.update(i.read_bytes())
            dir_dict[str(i)] = h.hexdigest()
        if i.is_dir():
            recurse_dir(i)


def main():
    recurse_dir(Path('.'))

    for k,v in sorted(dir_dict.items()):
        print(f'{k} -- {v}')


if __name__ == '__main__':
    main()
