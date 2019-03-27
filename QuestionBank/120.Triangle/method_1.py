#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/27 14:22
# @Author   : cancan
# @File     : method_1.py
# @Function : 三角形最小路径和


"""
Question:
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

Example，
给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

Note：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution:
	def minimumTotal(self, triangle):

		if not triangle:
			return 0

		for row in range(len(triangle) - 1, 0, -1):
			for col, _ in enumerate(triangle[row - 1]):
				triangle[row - 1][col] += \
					min(triangle[row][col], triangle[row][col + 1])

		return triangle[0][0]


s = Solution()
print(s.minimumTotal([
	[2],
	[3, 4],
	[6, 5, 7],
	[4, 1, 8, 3]
]))

print(s.minimumTotal([[-10]]))

print(s.minimumTotal([
	[-1],
	[2, 3],
	[1, -1, -1]
]))
