
# list数组的差分
from collections import defaultdict

t = [1, 3, 3, 6]
diff = [t[i+1]-t[i] for i in range(len(t)-1)]
print(diff)

# 数组跳变起始沿的index
t = [1, 3, 3, 6]
index = [i+1 for i in range(len(t)-1) if t[i+1]-t[i] != 0]
print(index)

#%% binary tree
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (float/int/str)
        self.left = left    # Left child
        self.right = right  # Right child
from binarytree import tree, bst, heap

# Generate a random binary tree and return its root node.
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node.
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node.
my_heap = heap(height=3, is_max=True, is_perfect=False)

# Pretty-print the trees in stdout.
print(my_tree)
#
#        _______1_____
#       /             \
#      4__          ___3
#     /   \        /    \
#    0     9      13     14
#         / \       \
#        7   10      2
#
print(my_bst)
#
#            ______7_______
#           /              \
#        __3__           ___11___
#       /     \         /        \
#      1       5       9         _13
#     / \     / \     / \       /   \
#    0   2   4   6   8   10    12    14
#
print(my_heap)
#
#              _____14__
#             /         \
#        ____13__        9
#       /        \      / \
#      12         7    3   8
#     /  \       /
#    0    10    6
#

##### build tree
from binarytree import build, build2, Node

# First let's create an example tree.
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(5)
print(root)
#
#           1
#          /
#       __2
#      /
#     3
#    / \
#   4   5

# First representation is already shown above.
# All "null" nodes in each level are present.
print(root.values)
# [1, 2, None, 3, None, None, None, 4, 5]

# Second representation is more compact but without the indexing properties.
print(root.values2)
# [1, 2, None, 3, None, 4, 5]

# Build trees from the list representations
tree1 = build(root.values)
tree2 = build2(root.values2)
assert tree1.equals(tree2) is True

# 斐波那契递归
def f(fn, fn_1, n):
    if n <= 1:
        return fn
    return f(fn_1 + fn, fn, n - 1)

print(f(1, 0, 4))

#
def findIndexLessThan(nums: list, target: int):
    left, right = -1, len(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    print(left)
    return left

findIndexLessThan([1,2,3], 1)
findIndexLessThan([1,2,3], 1.5)
findIndexLessThan([2], 1)

# def findIndexLargeThan(nums: list, target: int):
#     left, right = -1, len(nums)
#     while right - left > 1:
#         mid = (left + right) // 2
#         if nums[mid] <= target:
#             left = mid
#         else:
#             right = mid
#     print(right)
#     return right
#
# findIndexLargeThan([1,2,3], 1)
# findIndexLargeThan([2], 1)

import tqdm
import time

for i in tqdm.tqdm(range(100)):
    time.sleep(0.1)
    pass
