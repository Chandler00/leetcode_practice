# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:39:16 2018
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
#
#Example 1:
#
#Input: "()"
#Output: true
#Example 2:
#
#Input: "()[]{}"
#Output: true
#Example 3:
#
#Input: "(]"
#Output: false
#Example 4:
#
#Input: "([)]"
#Output: false
#Example 5:
#
#Input: "{[]}"
#Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

#            
        a = len(s)
        check =[]
        if s == '':
            return True
        
        if s[0] in [']','}',')']:
            
            return False
             
        brackets = {')':'(', '}':'{', ']':'['}  
#            
#            for i in range(a):
#                check.append(s[i])
#                if brackets[s[i-1]] == s[i]:
#                    check.pop()
                
        for i in s:
            
            check.append(i)
            
            if check[0] in [']','}',')']:
            
                return False
            
            if i in [')', ']', '}']:

                if brackets[check[-1]]==check[-2]:
                    
                    check=check[:-2]
        
        if len(check)>0:
            
            return False
        
        else:
            
            return True
                    
                

            
            
            
            
            
            
        
        
        