import random

from AVLTrees import *


def successors_check(t: AVLTree, keys: list):
    """
    Checks using successors:
    @param t: The tree to check
    @param keys: The keys that t should contain
    @return: Whether the tree is valid according to the preformed tests
    """
    if t.size() != len(keys):
        print("size: ", t.size())
        print("true size: ", len(keys))
        print("Wrong tree size!")
        return False

    if t.size() == 0:
        return True

    keys = sorted(keys.copy())
    t_keys = []

    m: AVLNode = t.get_root()
    while m.get_left().is_real_node():
        m = m.get_left()

    while m is not None:
        t_keys.append(m.get_key())
        m = t.successor(m)

    if t_keys != keys:
        print("Wrong values")
        return False

    return True


def inorder_walk_check(t: AVLTree, keys):
    """
    Checks tree size.
    If size is correct, checks using inorder-tree-walk:
        - nodes' sizes
        - nodes' heights
        - nodes' balance factor
        - nodes' pointers
        - tree's keys

    @param t: The tree to check.
    @param keys: The keys that t should contain
    @return: Whether the tree is valid according to the preformed tests
    """
    if t.size() != len(keys):
        print("size: ", t.size())
        print("true size: ", len(keys))
        print("Wrong tree size!")
        return False

    if t.size() == 0:
        return True

    keys = sorted(keys.copy())
    t_keys = []
    def rec(node, lst):
        if not node.is_real_node():
            has_error = (node.get_left() is not None) or (node.get_right() is not None)
            if has_error:
                print(f"One of the virtual nodes' sons is not None.")
            return 0, -1, has_error  # size, height, has error

        key = node.get_key()

        ls, lh, le = rec(node.get_left(), lst)
        lst.append(key)
        rs, rh, re = rec(node.get_right(), lst)

        has_error = le or re

        if node.get_size() != ls + rs + 1:
            has_error = True
        if node.get_height() != max(lh, rh) + 1:
            print(f"Wrong height of node {key}.")
            has_error = True

        bf = lh - rh
        if abs(bf) > 1:
            print(f"BF of node {key} is {bf}.")
            has_error = True
        if node.get_bf() != bf:
            print("bf: ", node.get_bf(), "height:" , node.get_height())
            print(f"Wrong BF of node {key}.")
            has_error = True

        if node.get_left().get_parent() is not node:
            print(f"Node {key} is not the parent of its left son.")
            has_error = True
        if node.get_right().get_parent() is not node:
            print(f"Node {key} is not the parent of its right son.")
            has_error = True

        return ls + rs + 1, max(lh, rh) + 1, has_error

    root = t.get_root()
    s, h, error = rec(root, t_keys)
    if t_keys != keys:
        print("Wrong keys in the tree!")
        error = True

    if root.get_parent() is not None:
        print("Tree's root's parent is not None!")
        error = True

    return not error


def print_error(keys, new_keys, action, curr_key):
    print(f"Problematic keys: {keys}")
    print(f"Problematic new keys: {new_keys}")
    print(f"Error while {action} {curr_key}")


def run(tests, val_range=100, t_size=2, tester=inorder_walk_check):
    """
    Runs a series of tests on random trees.
    You should implement insert, delete before running this tester.
    @param tests: How many random trees to test.
    @param val_range: The range of the keys of the random trees. Should be greater than t_size by a big number.
    @param t_size: The size of the random trees.
    @param tester: Which tester to run, default to inorder_walk_check.
    Prints the errors from the tests.
    """
    print(f"\nStarting {tests} tests, verifying with '{tester.__name__}()'.")

    err_cnt = 0
    for test_num in range(tests):
        t = AVLTree()
        keys = random.sample(range(val_range), t_size)
        new_keys = keys.copy()
        random.shuffle(new_keys)

        for i, key in enumerate(keys):
            try:
                t.insert(key, 0)
            except Exception:
                print_error(keys, new_keys, "inserting", key)
                print("Exception!")
                return t

            if not tester(t, keys[:i + 1]):
                print_error(keys, new_keys, "checking after inserted", key)
                err_cnt += 1

        for i, key in enumerate(new_keys):
            try:
                t.delete(t.search(key))
            except Exception:
                print_error(keys, new_keys, "deleting", key)
                print("Exception!")
                return t

            if not tester(t, new_keys[i + 1:]):
                print_error(keys, new_keys, "checking after deleted", key)
                err_cnt += 1

        if (test_num + 1) % 100 == 0:
            print(f"{test_num + 1} tests ran successfully.")

    print(f"\nDone {tests} tests with {err_cnt} errors and 0 exceptions.")


def debug(keys, new_keys, tester=inorder_walk_check):
    t = AVLTree()

    for i, key in enumerate(keys):
        try:
            t.insert(key, 0)
        except Exception:
            print_error(keys, new_keys, "inserting", key)
            return t

        if not tester(t, keys[:i + 1]):
            print_error(keys, new_keys, "checking after inserted", key)

    for i, key in enumerate(new_keys):
        t.delete(t.search(key))


        if not tester(t, new_keys[i + 1:]):
            print_error(keys, new_keys, "checking after deleted", key)

    print("Done!")


if __name__ == '__main__':
    # You should implement get_bf() in AVLNode to run:
    run(1, 100, 5, inorder_walk_check)
    debug([24, 2, 91, 17, 24], [91, 66, 2, 17, 24])

    # To run the second test you should implement get_successor(node) in AVLTree.
    # run(1000, 1000, 500, successors_check)
