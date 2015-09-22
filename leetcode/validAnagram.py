__author__ = 'Lily'

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if len(s)!=len(t):
            return False
        for i in s:
            for j in range(0,len(t)):
                if i==t[j]:
                    break
                if j==len(t)-1:
                    return False
        return True
    def isAnagram1(self,s,t):
        if len(s)!=len(t):
            return False
        temp=[0]*26
        for i in list(s):
            temp[ord(i)-ord('a')]+1
        for j in list(t):
            temp[ord(j)-ord('a')]-1
            if temp[ord(j)-ord('a')]<0:
                return False
        return True

solution=Solution()
print solution.isAnagram1("dgqztusjuu", "dqugjzutsu")