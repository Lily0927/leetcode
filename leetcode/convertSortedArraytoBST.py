__author__ = 'Lily'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if nums==None:
            return None
        return self.buildTree(nums,0,len(nums)-1)

    def buildTree(self,nums,start,end):
        if start>end:
            return None
        result=TreeNode(nums[(start+end)/2])
        result.left=self.buildTree(nums,start,(start+end)/2-1)
        result.right=self.buildTree(nums,start,(start+end)/2+1)
        return result