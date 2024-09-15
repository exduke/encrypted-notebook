"""
@describe:
@fileName: miller_rabin.py
@time    : 2024/6/11 15:50
@author  : duke
"""
P_LIST = (2, 3, 5, 7, 11, 13, 19, 23, 29, 31)


def check(x: int) -> bool:
    for p in P_LIST:
        if x == p:
            return True
        if x % p == 0:
            return False

    for p in P_LIST:
        k = x - 1
        k *= 2
        while k % 2 == 0:
            k = k // 2
            t = pow(p, k, x)
            if t == x - 1:
                break
            if t == 1:
                continue
            return False

    return True
