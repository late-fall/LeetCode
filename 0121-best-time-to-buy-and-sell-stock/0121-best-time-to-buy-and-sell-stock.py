class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 1:
#             return 0
#         profit = prices[1] - prices[0]
        
       
#         start = 0
#         for i in range(len(prices)-1):
#             if prices[i] > prices[i+1]:
#                 start = i
                
#         for start in range(len(prices)):
#             for j in range(start+1,len(prices)):
#                 if prices[j] - prices[start] > profit:
#                     profit = prices[j] - prices[start]
#         return profit if profit > 0 else 0

#         NOTE
#         uses two pointers
#         left = buy, right = sell pointer
#         if right is less than left, left becomes right and update right pointer.
#         if left < right, leave the left pointer and update right pointer. 
        
#         memory : O(1)
#         time : O(N)
            
        l, r = 0, 1 # left is buying, right is selling. 
        maxProfit = 0
        
        while r < len(prices):
            # profit?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit