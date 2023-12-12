class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_a = list(reversed(a))
        list_b = list(reversed(b))
                
        res = []
        
        i = 0
        carry = 0
        
        while i < max(len(a),len(b)):
            da = 0 if i >= len(a) else int(list_a[i])
            db = 0 if i >= len(b) else int(list_b[i])
            digit = da + db + carry
            if digit <= 1:
                res.append(str(digit))
                carry = 0
            else:
                res.append(str(digit%2))
                carry = 1
            i += 1
        
        if carry == 1:
            res.append('1')
        
        res.reverse()
        
        return ''.join(res)