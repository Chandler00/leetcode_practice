# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:20:07 2019
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""

#Given a binary tree, find its maximum depth.
#
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#Note: A leaf is a node with no children.
#
#Example:
#
#Given binary tree [3,9,20,null,null,15,7],
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its depth = 3.


# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        
        if root is None:
            return 0
        else:
            
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
        return max(left, right) + 1
            
    