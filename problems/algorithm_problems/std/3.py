#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    n = int(input())
    q = deque()
    inp = input().split()
    for el in inp:
        if el.isdigit():
            x = int(el)
            q.append(x)
        else:
            b, a = q.pop(), q.pop()
            match el:
                case '+':
                    q.append(a + b)
                case '-':
                    q.append(a - b)
                case '*':
                    q.append(a * b)
    print(q[-1])
