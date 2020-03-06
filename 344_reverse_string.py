# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:26:21 2018
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""

#Write a function that takes a string as input and returns the string reversed.
#
#Example 1:
#
#Input: "hello"
#Output: "olleh"
#Example 2:
#
#Input: "A man, a plan, a canal: Panama"
#Output: "amanaP :lanac a ,nalp a ,nam A"


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        rev=''
        for i in range(length):
            
            rev+=s[-i-1]
        
        return rev
