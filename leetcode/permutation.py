__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    result=[]
    def permute(self, nums):
        resultTem=[]
        temp=[1]*len(nums)
        remain=len(nums)
        self.dfs(nums,remain,resultTem,temp)
        return self.result

    def dfs(self,nums,remain,resultTem,temp):

        if remain==0:
            self.result.append(resultTem)
            return
        for i in range(0,len(nums)):
            if temp[i]!=0:

                a=resultTem[:]
                a.append(nums[i])
                b=temp[:]
                b[i]-=1

                self.dfs(nums,remain-1,a,b)


solution=Solution()
print solution.permute([0,1])

