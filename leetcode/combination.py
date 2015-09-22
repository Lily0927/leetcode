__author__ = 'Lily'


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def __init__(self):
        self.result=[]
    def combine(self, n, k):
        self.dfs(k,n-k,[])
        return self.result


    def dfs(self,chose,nochose,array):
        temp=[]
        if chose==0 and nochose==0:
            for i in range(0,len(array)):
                if array[i]==1:
                    temp.append(i+1)
            self.result.append(temp)

        if chose>0:
            temp1=array[:]
            temp1.append(1)
            self.dfs(chose-1,nochose,temp1)
        if nochose>0:
            temp1=array[:]
            temp1.append(0)
            self.dfs(chose,nochose-1,temp1)


s=Solution()

print s.combine(4,2)