class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    nums = []
    recur_sum(root, '', nums)
    return sum(nums)


def recur_sum(root, num_string, nums):
    if root is None:
        return 0

    num_string = num_string + str(root.val)
    # print(num_string)

    if root.left is None and root.right is None:
        val = int(num_string)
        nums.append(val)

    recur_sum(root.left, num_string, nums)
    recur_sum(root.right, num_string, nums)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
