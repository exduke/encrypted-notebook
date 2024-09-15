"""
@describe:
@fileName: rsa_local.py
@time    : 2024/6/11 12:50
@author  : duke
"""
import math
import src.utils.miller_rabin as miller_rabin


class IterBytes2Int:
    def __init__(self, content: bytes, offset: int = 4):
        self.offset = offset
        r = len(content) % self.offset
        if r:
            content += b'\x00' * (self.offset - r)
        self.content = content

    def __iter__(self):
        self.index = 0
        self.length = len(self.content)
        return self

    def __next__(self):
        self.index += self.offset
        if self.index > self.length:
            raise StopIteration
        return int.from_bytes(self.content[self.index - self.offset:self.index])


def encode(content: bytes, e: int, n: int) -> bytes:
    """
    encode
    :param content: bytes
    :return: bytes
    """
    offset = 1
    while 256 ** offset < n:
        offset += 1

    result = bytes()
    for i in IterBytes2Int(content, offset=offset - 1):
        result += pow(i, e, n).to_bytes(length=offset, byteorder='big')
    return result


def decode(content: bytes, d: int, n: int) -> bytes:
    """
    decode
    :param content: bytes
    :return: bytes
    """
    offset = 1
    while 256 ** offset < n:
        offset += 1

    result = bytes()
    for i in IterBytes2Int(content, offset=offset):
        result += pow(i, d, n).to_bytes(length=offset - 1, byteorder='big')
    while result[-1] == 0:
        result = result[:-1]
    return result


def summon_key_from_md5(md5: str) -> tuple:
    """
    summon n, e, d from input md5 str
    :param md5: hex str
    :return: (n, e, d)
    """
    md5_bytes = bytes.fromhex(md5)
    num1, num2 = 0, 0
    for i in range(len(md5_bytes)):
        num1 ^= int.from_bytes(md5_bytes[i:i + 1]) << (i % 4) * 8
        num2 ^= int.from_bytes(md5_bytes[i:i + 1]) << (i // math.ceil(len(md5_bytes) / 4)) * 8

    if num1 % 2 == 0:
        num1 += 1
    if num2 % 2 == 0:
        num2 += 1

    # safe prime num, which means num is prime and (num - 1) // 2 is prime
    while not (miller_rabin.check(num1) and miller_rabin.check((num1 - 1) // 2)):
        num1 += 2
    while not (miller_rabin.check(num2) and miller_rabin.check((num2 - 1) // 2)):
        num2 += 2

    n = num1 * num2
    l = math.lcm(num1 - 1, num2 - 1)

    # 65537
    e = 2 ** 16 + 1
    while math.gcd(e, l) != 1:
        e += 2

    if e > l:
        raise Exception('e > l')

    d = l - l // e

    r = (e * d) % l
    while r != 1:
        if r > e:
            d -= 1
        else:
            d -= l // e
        r = (e * d) % l

    if d < 0:
        raise Exception('d < 0')

    return n, e, d
