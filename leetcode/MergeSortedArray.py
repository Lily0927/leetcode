__author__ = 'Lily'

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index=m+n
        while m>0 and n>0:

            if nums1[m-1]>nums2[n-1]:
                index-=1
                n-=1
                nums1[index]=nums1[n]
            else:
                index-=1
                n-=1
                nums1[index]=nums2[n]
        while n>0:
            index-=1
            n-=1
            nums1[index]=nums2[n]

