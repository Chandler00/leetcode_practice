# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:52:05 2018
Team : Advacned Analytics
Author: Chandler Qian
Content : 
"""

#169. Majority Element
#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
#You may assume that the array is non-empty and the majority element always exist in the array.
#
#Example 1:
#
#Input: [3,2,3]
#Output: 3
#Example 2:
#
#Input: [2,2,1,1,1,2,2]
#Output: 2

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lth = len(nums)
#        unique = set(nums)
#        counts={}
#        
#        for i in unique:
#            counts[i]=0
#            
#        for number in nums:
#            
#            counts[number]+=1
#            
#            if  counts[number] > (lth/2):
#                
#                return number
#            
#        return max(counts, key=counts.get)
        
        lth = len(nums)
        num_sort = sorted(nums)
        return num_sort[lth//2+lth%2-1]
        
#            