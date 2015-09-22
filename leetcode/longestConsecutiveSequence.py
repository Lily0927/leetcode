__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        store={}
        n=0
        for i in nums:
            store[i]=n
            n=n+1
        maxl=1

        for i in nums:
            if store.get(i)==1:
                continue
            temp=i
            current_max=1
            while temp-1 in store:
                temp-=1
                current_max+=1
                store[temp]=1
            temp=i
            while temp+1 in store:
                temp+=1
                current_max+=1
                store[temp]=1
            maxl=max(maxl,current_max)
        return maxl

solution=Solution()
print solution.longestConsecutive([1,2,0,1])