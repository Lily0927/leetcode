__author__ = 'Lily'


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dics = {}
        dict = {}
        for i in range(0, len(s)):
            if s[i] in dics and t[i] in dict:
                if dics[s[i]]!=dict[t[i]]:
                    return False
            elif s[i] in dics or t[i] in dict:
                return False
            else:
                dics[s[i]]=i
                dict[t[i]]=i
        return True


solution = Solution()
print solution.isIsomorphic('abb', 'aca')