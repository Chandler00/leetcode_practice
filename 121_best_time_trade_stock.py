# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:28:05 2018
Team : Advanced Analytics
Author: Chandler Qian
Content : 
"""


#Say you have an array for which the ith element is the price of a given stock on day i.
#
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
#Note that you cannot sell a stock before you buy one.
#
#Example 1:
#
#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#             Not 7-1 = 6, as selling price needs to be larger than buying price.
#Example 2:
#
#Input: [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.



class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p_max = 0
        d_length= (len(prices))
        if d_length==0:
            return 0
        min_po = prices[0] 
        for i in range(d_length):
            if min_po >prices[i] : min_po = prices[i]  

            if ((prices[i] - min_po) > p_max) : p_max = (prices[i] - min_po)
        
        return p_max
            
            
        
        
        
        
        