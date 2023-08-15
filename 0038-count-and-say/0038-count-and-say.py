class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        res = ""
        count = 0
        curr = prev[0]
        
        for num in prev:
            if num == curr:
                count += 1
            else:
                res += str(count)
                res += str(curr)
                curr = num
                count = 1
        res += str(count)
        res += str(curr)
        return res