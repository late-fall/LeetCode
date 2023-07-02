class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = {"2":['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],'6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        for d in digits:
            temp = []
            if len(res) == 0:
                temp = letters[d]
            else:
                for item in res:
                    for l in letters[d]:
                        temp.append(item + l)
            res = temp
        return res
                