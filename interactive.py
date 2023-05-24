from AVLTree import AVLTree, AVLNode

def print_tree(t: AVLTree):
    out = ""
    if t.get_root() is not None:
        for row in t_repr(t.get_root()):  # need printree.py file
            out = out + row + "\n"
    print(out)


def t_repr(n: AVLNode):
    n_repr = f"{n.key},{n.get_bf()},{n.get_height()}"

    if not n.is_real_node():
        return ["#"]

    if n.is_leaf():
        return [n_repr]

    return concat(t_repr(n.left), n_repr, t_repr(n.right))


def concat(left, root, right):
    l_w = len(left[-1])
    r_w = len(right[-1])
    root_w = len(root)

    result = [(l_w + 1) * " " + root + (r_w + 1) * " "]

    ls = left_space(left[0])
    rs = right_space(right[0])
    result.append(ls * " " + (l_w - ls) * "_" + "/" + root_w * " " + "\\" + rs * "_" + (r_w - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += l_w * " "

        row += (root_w + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += r_w * " "

        result.append(row)

    return result


def left_space(row):
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def right_space(row):
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


def interactive(t=None):
    if t is None:
        t = AVLTree()

    while True:
        message = "Choose action: \n" \
                  "\t(1) print tree\n" \
                  "\t(2) insert\n" \
                  "\t(3) delete\n" \
                  "\t(4) search\n" \
                  "\t(5) size\n" \
                  "\t(6) successor\n" \
                  "\t(e) exit"
        print(message)
        choice = input(">>>")

        if choice == "e":
            return t

        if not choice.isdigit():
            print("Invalid input.\n")
            continue

        choice = int(choice)
        if choice < 1 or choice > 6:
            print("Invalid input.\n")
            continue

        if choice == 1:
            print_tree(t)

        if choice == 2:
            while True:
                key = input("insert key (e to exit): ")
                if key == "e":
                    break

                if not key.isdigit():
                    print("Invalid input.")
                    continue

                key = int(key)
                if t.search(key) is not None:
                    print(f"The tree already contains {key}.")
                    continue

                balance_ops = t.insert(key, 0)
                print(f"Inserted {key}, {balance_ops = }\n")
                break

        if choice == 3:
            while True:
                key = input("delete key (e to exit): ")
                if key == "e":
                    break

                if not key.isdigit():
                    print("Invalid input.")
                    continue

                key = int(key)
                node = t.search(key)
                print(node)
                if node is None:
                    print(f"The tree doesn't contain {key}.")
                    continue

                balance_ops = t.delete(node)
                print(f"Deleted {key}, {balance_ops = }\n")
                break

        if choice == 4:
            while True:
                key = input("search key (e to exit): ")
                if key == "e":
                    break

                if not key.isdigit():
                    print("Invalid input.")
                    continue

                key = int(key)
                print(t.search(key))
                is_inside = not t.search(key) is None
                print(f"{key} is{'' if is_inside else ' not'} in the tree.\n")
                break

        if choice == 5:
            print(f"Tree size: {t.size()}\n")

        if choice == 6:
            while True:
                key = input("successor of key (e to exit): ")
                if key == "e":
                    break

                if not key.isdigit():
                    print("Invalid input.")
                    continue

                key = int(key)
                node = t.search(key)
                if node is None:
                    print("n: ",node)
                    print(f"The tree doesn't contain {key}.")
                    continue

                successor = t.get_successor(node)
                if successor is None:
                    print(f"No successor, {key} is the maximum.\n")
                else:
                    print(f"The successor is {successor.get_key()}.\n")

                break
    return t


if __name__ == '__main__':
    interactive()
