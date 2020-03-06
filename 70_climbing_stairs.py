# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:28:30 2018
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""

#70. Climbing Stairs
#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#Note: Given n will be a positive integer.
#
#Example 1:
#
#Input: 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:
#
#Input: 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step

from math import factorial

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step2 = n // 2
        result = 1
        for i in range(1, step2+1):
            
            ranks = n - i
            result += factorial(ranks)/(factorial(i)*factorial(ranks-i))
            
        return int(result)

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        p1, p2 = 2, 1
        for _ in range(n - 2):
            p1, p2 = p1 + p2, p1
        return p1
        
