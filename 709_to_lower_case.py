# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:28:50 2019
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""

#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
# 
#
#Example 1:
#
#Input: "Hello"
#Output: "hello"
#Example 2:
#
#Input: "here"
#Output: "here"
#Example 3:
#
#Input: "LOVELY"
#Output: "lovely"


class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new = ''
        for i in str:
             new+=i.lower()
        return new