#!/usr/bin/env python
# @Time     : 2018/5/12 下午5:52
# @Author   : cancan
# @File     : question_3.py
# @Function : 对称二叉树

"""
Question:
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

Note:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        t = []
        n = []
        def f(node, t, n):
            if node.left:
                t.append(node.left)
                n.append(node.left.val)
            else:
                n.append(None)
            if node.right:
                t.append(node.right)
                n.append(node.right.val)
            else:
                n.append(None)
        f(root, t, n)
        while t:
            l = len(n)
            for _ in range(l // 2):
                if n[_] != n[l - _ - 1]:
                    return False
            p = []
            n = []
            for i in t:
                f(i, p, n)

            t = p

        return True


if __name__ == "__main__":
    a = Solution()
    root = stringToTreeNode('[1,2,3,3,null,2,null]')
    print(a.isSymmetric(root))
