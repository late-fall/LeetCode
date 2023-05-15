class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = int(a) + int(b)
        num_str = str(num)
        num_rev = list(num_str[::-1])
        
        carry = 0
        for i in range(len(num_rev)):
            if carry == 1:
                num_rev[i] = str(int(num_rev[i]) + 1)
            if num_rev[i] == '2':
                num_rev[i] = '0'
                carry = 1
            elif num_rev[i] == '3':
                num_rev[i] = '1'
                carry = 1
            else:
                carry = 0
            if i == len(num_rev) -1 and carry == 1:
                num_rev += '1'
        
        print(num_rev)
        return ''.join(num_rev)[::-1]
        