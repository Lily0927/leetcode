__author__ = 'Lily'

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if digits is None:
            return None
        n =len(digits)
        if digits[n-1]!=9:
            digits[n-1]+=1
            return digits
        else:
            add=1
            for i in range(n-1,-1,-1):
                temp=digits[i]+add
                digits[i]=temp%10
                add=temp/10
                if add==0:
                    return digits
                if i ==0 and add!=0:
                    digits.insert(0,1)

        return digits

solution=Solution()
print solution.plusOne([9])