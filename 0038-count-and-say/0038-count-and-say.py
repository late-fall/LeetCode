class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: 
            return "1"
        res = "1"
        for i in range(n-1):
            say = ""
            while res:
                say += str(len(res) - len(res.lstrip(res[0]))) + res[0]
                res = res.lstrip(res[0])      
            res = say

        return res