"""
@describe:
@fileName: algorithm.py
@time    : 2025/8/16 1:23
@author  : duke
"""
import os
import time
from hashlib import md5
import struct
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# import json


def get_time_stamp_md5():
    ts = time.time()
    ts_bytes = struct.pack('>d', ts)
    return md5(ts_bytes).digest()


def encode(data, key):
    iv = get_time_stamp_md5()
    cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    data = cipher_cbc.encrypt(pad(data, AES.block_size))
    data += cipher_ecb.encrypt(iv)
    return data


def decode(data, key):
    iv = data[-16:]
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    iv = cipher_ecb.decrypt(iv)
    cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
    data = data[:-16]
    data = unpad(cipher_cbc.decrypt(data), AES.block_size)
    return data


def get_sorted_files(dir_path, key=int):
    files = os.listdir(dir_path)
    files.sort(key=key)
    return files
