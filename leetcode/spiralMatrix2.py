__author__ = 'Lily'

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result=[[0 for x in range(0,n)] for x in range(0,n)]
        direct=0
        x=0
        y=0
        for i in range(1,n*n+1):
            result[x][y]=i
            tempx,tempy=self.direction(direct,x,y)

            if (not (0<=tempy<n and 0<=tempx<n)) or result[tempx][tempy]!=0:
                direct=(direct+1)%4
                tempx,tempy=self.direction(direct,x,y)

            x=tempx
            y=tempy
        return result

    def direction(self,direct,x,y):
        if direct==0:
            tempx=x
            tempy=y+1
        elif direct==1:
            tempx=x+1
            tempy=y
        elif direct==2:
            tempx=x
            tempy=y-1
        elif direct==3:
            tempx=x-1
            tempy=y
        return tempx,tempy