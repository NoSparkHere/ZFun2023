#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input())
    f = [0, 1, 1]
    for i in range(3, 91):
        f.append(f[-1] + f[-2])
    for i in range(n):
        print(f[int(input())])
    