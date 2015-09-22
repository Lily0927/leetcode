__author__ = 'Lily'


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        store={}
        index=0
        for i in nums:
            if i in store:
                first=store[i]
                differ=index-first
                if differ<=k:
                    return True
                else:
                    store[i]=index
                    index+=1
            else:
                store[i]=index
                index+=1
        return False
solution=Solution()
print solution.containsNearbyDuplicate([1,2,1,1],1)
