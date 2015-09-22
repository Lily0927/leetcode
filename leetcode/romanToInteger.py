__author__ = 'Lily'

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        store={}
        store['I']=1
        store['V']=5;
        store['X']=10;
        store['L']=50;
        store['C']=100;
        store['D']=500;
        store['M']=1000;
        result=0
        for i in range(len(s)-1,-1,-1):
            if i== len(s)-1:
                result+=store[s[i]]
                continue
            if store[s[i]]>store[s[i+1]]:
                result+=store[s[i]]
            else:
                result-=store[s[i]]
        return result
solution=Solution()
print solution.romanToInt('IV')