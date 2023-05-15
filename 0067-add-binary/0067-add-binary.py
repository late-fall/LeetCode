class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = int(a) + int(b)
        num_str = str(num)
        num_rev = list(num_str[::-1])
        
        add = 0
        for i in range(len(num_rev)):
            if add == 1:
                num_rev[i] = str(int(num_rev[i]) + 1)
            if num_rev[i] == '2':
                num_rev[i] = '0'
                add = 1
            elif num_rev[i] == '3':
                num_rev[i] = '1'
                add = 1
            else:
                add = 0
            if i == len(num_rev) -1 and add == 1:
                num_rev += '1'
        
        print(num_rev)
        return ''.join(num_rev)[::-1]
        