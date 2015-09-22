__author__ = 'Lily'

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result=[]
        for i in range(0,numRows):
            row=[0]*(i+1)
            if i ==0:
                row[i]=1
            elif i==1:
                row[0]=1
                row[1]=1
            else:
                for j in range(0,i):
                    if j ==0:
                        row[0]=1
                    else:
                        row[j]=result[i-1][j-1]+result[i-1][j]
                row[i]=1
            result.append(row)
        return result
solution=Solution()
print solution.generate()
