#import random library
import random

#define 3x3 matrix
matrix= [[1,2,3],[4,5,6],[7,8,9]] 

#matrix row loop
for i in range(3):
    #matrix column loop
    for j in range(3):
        while True:
            temp=1
            randomint=random.randint(0,100)
            if randomint==1:
                continue
            elif randomint==2:
                matrix[i][j]=randomint
                break
            else:
                for h in range (2, randomint):
                    if randomint%h==0:
                        temp=0
                        continue
                if temp==0:
                    continue
                else:   
                    matrix[i][j]=randomint
                    break
                         
#print matrix to screen        
print(matrix)

