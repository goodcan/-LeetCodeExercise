#!/usr/bin/env python
# @Time     : 2018/4/7 下午10:52
# @Author   : cancan
# @File     : question_5.py
# @Function : 从排序数组中删除重复项

"""
Question:
给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。

Example:
给定数组: nums = [1,1,2],
你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
不需要理会新的数组长度后面的元素
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        d = []
        for i, v in enumerate(nums):
            if v not in a:
                a.append(v)
            else:
                d.append(i)

        for i in sorted(d, reverse=True):
            del nums[i]

        return len(nums)
