class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        arr = []
        res = []
        for n in nums:
            hashmap[n] += 1
        for n in hashmap:
            arr.append([n,hashmap[n]])
        arr.sort(key = lambda x: x[1])
        for i in range(k):
            res.append(arr[-(i+1)][0])
        return res