# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:49:13 2018
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""
#Example 1:
#
#Input: A = [1], K = 0
#Output: 0
#Explanation: B = [1]
#Example 2:
#
#Input: A = [0,10], K = 2
#Output: 6
#Explanation: B = [2,8]
#Example 3:
#
#Input: A = [1,3,6], K = 3
#Output: 3
#Explanation: B = [4,6,3]

# solutionWe can formalize the above concept: if A[i] < A[j], we don't need to consider when A[i] goes down while A[j] goes up. This is because the interval (A[i] + K, A[j] - K) is a subset of (A[i] - K, A[j] + K) (here, (a, b) for a > b denotes (b, a) instead.)
#
#That means that it is never worse to choose (up, down) instead of (down, up). We can prove this claim that one interval is a subset of another, by showing both A[i] + K and A[j] - K are between A[i] - K and A[j] + K.
#
#For sorted A, say A[i] is the largest i that goes up. Then A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K are the only relevant values for calculating the answer: every other value is between one of these extremal values.


class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans
#    
class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        print(A)
        mva, nva = A[-1], A[0]
        result = mva-nva
        for i in range(len(A)-1):
            a, b = A[i], A[i+1]
            result = min(result, max(mva-K, a+K) - min(nva+K, b-K))
        return result
            
            
            
