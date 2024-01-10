class Solution:
    def maxProduct(self, s: str) -> int:
        # Brute force is OK, only small optimization possible
        # Need to use Bit Mask
        # for leetcodecom, ete would be 01010001000, and cdc is 00001010100
        # to check if they are disjoint. logic & will return 0 if disjoint.
        
        # goes from i=1 to 2**11 -1 (which is 1111111111)
        # hashmap[key = binary representation of the string], value is length of panlindrome.
        # use hashmap to calculate the max value. 
        
        # time complexity is 4**n
        
        n = len(s)
        pali = {} #binary representation of string : length
        
        for mask in range(1, 1 << n): # 1 << n == 2 ** n, slightly more efficient. 
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)
        
        #find longest
        longest = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0: # meaning they are disjoint.
                    longest = max(longest, pali[m1] * pali[m2])
        
        return longest