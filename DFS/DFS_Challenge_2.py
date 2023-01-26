import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class max_path_sum:

    def __init__(self, root):
        self.root = root
        self.max_path = -math.inf

    def find_maximum_path_sum(self):
        self.find_maximum_path_sum_recur(self.root)
        return self.max_path

    def find_maximum_path_sum_recur(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        cur_sum = root.val

        max_left_node_child_val = self.find_maximum_path_sum_recur(root.left)
        max_right_node_child_val = self.find_maximum_path_sum_recur(root.right)
        cur_sum = max(cur_sum, root.val + max_left_node_child_val + max_right_node_child_val)

        self.max_path = max(self.max_path, cur_sum)

        return max(root.val + max_left_node_child_val, root.val + max_right_node_child_val)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    max_path_finder = max_path_sum(root)

    print("Maximum Path Sum: " + str(max_path_finder.find_maximum_path_sum()))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(max_path_finder.find_maximum_path_sum()))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    max_path_finder = max_path_sum(root)
    print("Maximum Path Sum: " + str(max_path_finder.find_maximum_path_sum()))


main()
