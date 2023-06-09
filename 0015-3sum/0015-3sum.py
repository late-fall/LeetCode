class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         time: O(nlogn) + o(n**2) == O(n)
#         memory: O(n)
        numSorted = sorted(nums)
        print(numSorted)
        res = []
        
        for i, n in enumerate(numSorted):
            if i > 0 and numSorted[i-1] == numSorted[i]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                if n + numSorted[l] + numSorted[r] > 0:
                    r -= 1
                elif n + numSorted[l] + numSorted[r] < 0:
                    l += 1
                else:
                    res.append([n,numSorted[l],numSorted[r]])
                    l += 1
                    while numSorted[l] == numSorted[l-1] and l <r:
                        l += 1
        return res
        
        
#         numSorted = sorted(nums)
#         i = 0
#         res = []
#         while i < len(nums)-2 and numSorted[i] <= 0:
#             for j in range(i+1,len(numSorted)-1):
#                 val = -(numSorted[i] + numSorted[j])
#                 remaining = len(numSorted[j+1:])
#                 l, h = 0, remaining - 1
#                 while l <= h:
#                     mid = (l + h) // 2
#                     if val == numSorted[j+1:][mid]:
#                         newList = sorted([numSorted[i],numSorted[j],val])
#                         if newList not in res:
#                             res.append(newList)
#                         break
#                     elif val > numSorted[j+1:][mid]:
#                         l = mid + 1
#                     else:
#                         h = mid -1
                
                
#                 # if numSorted[j] +numSorted[i] > 0:
#                 #     return res
#                 # for k in range(j+1, len(numSorted)):
#                 #     if numSorted[i] + numSorted[j] + numSorted[k] > 0:
#                 #         break
#                 #     if numSorted[i] + numSorted[j] + numSorted[k] == 0:
#                         # newList = sorted([numSorted[i],numSorted[j],numSorted[k]])
#                         # if newList not in res:
#                         #     res.append(newList)
#             i += 1
#         return res