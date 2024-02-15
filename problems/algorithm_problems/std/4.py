#!/usr/bin/env python3

# import time

def main():
    n, m = [int(x) for x in input().split()]
    itemList = []
    f = [0 for _ in range(m + 1)]
    for i in range(n):
        wi, vi, ti = [int(x) for x in input().split()]
        itemList.append((wi, vi, ti))
    for wi, vi, ti in itemList:
        iter_range = range(m, wi - 1, -1) if ti else range(wi, m + 1)
        for i in iter_range:
            f[i] = max(f[i], f[i - wi] + vi)
    print(f[m])


if __name__ == '__main__':
    # t0 = time.process_time_ns()
    main()
    # t1 = time.process_time_ns()
    # print((t1 - t0) / 1000000)
