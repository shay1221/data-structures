import random

from AVLTree import *


def catch(*_):
    cnt = 0
    while True:
        t = AVLTree()
        keys = random.sample(range(500), 3)  # change if you want
        new_keys = keys.copy()
        random.shuffle(new_keys)

        for key in keys:
            t.insert(key, 0)
        for key in new_keys:
            try:
                #t.delete(t.search(key))
                t.delete(t.search(key))


            except Exception:
                print(keys)
                print(new_keys)
                print(f"Error while deleting {key}")
                return

        if cnt % 100 == 0:
            print(cnt)

        cnt += 1


if __name__ == '__main__':
    catch()
