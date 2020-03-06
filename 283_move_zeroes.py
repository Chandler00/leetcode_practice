# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:32:11 2018
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""
#
#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
#Example:
#
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Note:
#
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
#        count_z = 0
#        index = 0
#        for i in nums:
#            print(i)
#            if i == 0:
#                
#                nums.pop(index-count_z)
#                nums.append(0)
#                count_z+=1
#            
#            index+=1
#        
#        return nums
        count_z = 0
        lth = len(nums)
        for index in range(lth):

            if nums[index-count_z] == 0:
                
                nums.pop(index-count_z)
                nums.append(0)
                count_z+=1
            
            index+=1
        

                

        