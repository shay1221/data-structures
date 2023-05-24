import random

from AVLTree import *
from interactive import *


def catch(*_):
    t = AVLTree()

    t.insert(1,0)
    t.insert(3,0)
    t.insert(2,0)
    t.insert(5,0)
    t.insert(4,0)
    z = AVLNode(2,0,True)
    #t.insert_bst(z)
    #t.insert(5,0)
    #t.insert(4,0)
    k = t.get_root()
    print(k)

    #print(t.find_Node(0, "r"))
if __name__ == '__main__':
    catch()
