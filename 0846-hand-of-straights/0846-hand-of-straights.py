import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        handMap = Counter(hand)
        handHeap = []
        for key in handMap.keys():
            heapq.heappush(handHeap, key)
        
        while handHeap:
            first = handHeap[0]
            
            for i in range(first, first + groupSize):
                if i not in handMap:
                    return False
                handMap[i] -= 1
                if handMap[i] == 0:
                    if i != handHeap[0]:
                        return False
                    heapq.heappop(handHeap)
                           
        return True
        
#         if len(hand) % groupSize != 0:
#             return False
#         count = 0
#         hand.sort()
        
#         groups = [[] for x in range(groupSize)]
#         skip = set()
        
#         cur = 0
#         prev = -1
#         i = 0
#         while i < len(hand):
#             if i not in skip:
#                 if hand[i] == prev:
#                     skip.add(i)
#                 else:
#                     if len(groups[cur]) == groupSize:
#                         cur += 1
#                     groups[cur].append(hand[i])
#             prev = hand[i]
#             i = i + 1 if len(skip) == 0 else min(skip)
        