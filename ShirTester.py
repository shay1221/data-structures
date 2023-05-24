import random

from AVLTrees import *
from interactive import *


def catch(*_):
    root = AVLNode(8, 1)
    t = AVLTree()
    t.insert(3,1)
    t.insert(2,2)
    t.insert(4,3)
    m = AVLTree()
    m.insert(11,1)
    
    t.insert(5,3)
    t.insert(1,1)
    t.join(m,6,6)
    k = t.split(t.search(6))[0].get_root()
    print(k)
    #print(t.find_Node(0, "r"))
if __name__ == '__main__':
    catch()
