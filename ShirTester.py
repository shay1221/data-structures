import random

from AVLTree import *
from interactive import *


def catch(*_):
    root = AVLNode(1, 1)
    t = AVLTree()
    t.insert(1,1)
    t.insert(2,2)
    print(t.get_root().get_left())
if __name__ == '__main__':
    catch()
