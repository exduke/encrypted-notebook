"""
@describe:
@fileName: cfg.py
@time    : 2024/6/11 12:50
@author  : duke
"""
import os
import sys

DEV = False

# root path
if DEV:
    # pycharm
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    ROOT_PATH = os.path.dirname(ROOT_PATH)
else:
    # pyinstaller
    ROOT_PATH = os.path.dirname(os.path.abspath(sys.executable))

# data path
DATA_PATH = ROOT_PATH + '\\data'

# web path
if DEV:
    WEB_PATH = r'D:\Workspace\project\solution\encryted-notebook\encrypted-notebook-webui\dist'
else:
    WEB_PATH = ROOT_PATH + '\\web'

PORT = 23333

if __name__ == '__main__' and DEV:
    print(ROOT_PATH)
