# Uses python3
import sys
import itertools
import math


def partition3(arr):
    n=len(arr)
    sum = 0
    i, j = 0, 0
      
    # calculate sum of all elements 
    for i in range(n): 
        sum += arr[i] 
      
    if sum % 3 != 0: 
        return False 
      
    part = [[ True for i in range(n + 1)]  
                   for j in range(sum // 3 + 1)] 
      
    for i in range(0, n + 1): 
        part[0][i] = True
          
    for i in range(1, sum // 3 + 1): 
        part[i][0] = False
      
    for i in range(1, sum // 3 + 1): 
          
        for j in range(1, n + 1): 
            part[i][j] = part[i][j - 1] 
              
            if i >= arr[j - 1]: 
                part[i][j] = (part[i][j] or 
                              part[i - arr[j - 1]][j - 1]) 
          
    return part[sum // 3][n] 
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    x=partition3(A)
    if(x==True):
        print(1)
    else:
        print(0)

