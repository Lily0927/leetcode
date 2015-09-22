__author__ = 'Lily'

class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        resulttemp=[]
        remain=n
        i=1
        result=[]
        self.dfs(n,remain,resulttemp,i,k,result)
        return result

    def dfs(self,n, remain,resultTemp,i,k,result):
        if remain==0 and k==0:
            result.append(resultTemp)
            return
        if k==0:
            return
        for j in range(i,10):
            a=resultTemp[:]
            a.append(j)

            self.dfs(n,remain-i,a,j+1,k-1,result)



