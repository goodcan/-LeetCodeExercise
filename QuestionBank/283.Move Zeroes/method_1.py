#!/usr/bin/env python
# @Time     : 2018/5/1 下午9:30
# @Author   : cancan
# @File     : method_1.py
# @Function : 移动零

"""
Question:
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。
例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

Note:
1.必须在原数组上操作，不要为一个新数组分配额外空间。
2.尽量减少操作总数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = []
        for i, v in enumerate(nums):
            if v == 0:
                n.append(i)
        l = len(n)
        n = reversed(n)
        for i in n:
            del nums[i]

        nums.extend([0] * l)
