#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def inOrder(tree):
    result = []
    temp=[]
    i=0;j=0
    temp.append(i)
    
    flag=0
    while(flag==0):
        if(tree[j][1] != (-1)):
            temp.append(tree[j][1])
            j=tree[j][1]
        else:
            if len(temp)!= 0:
                x=temp.pop()
                #if tree[x][0] == result[len(result)-1]:
                    #return False
                #print(len(result))
                if len(result)>0 and  result[len(result)-1] > tree[x][0]:
                    return False
                #print(x)
                lft=tree[x][1]
                #print(lft)
                if lft != (-1):
                    if tree[lft][0] == tree[x][0]:
                        return False
                
                result.append(tree[x][0])
                #print(result)
                if(tree[x][2] != (-1)):
                    temp.append(tree[x][2])
                    j=tree[x][2]
            else:
                flag=1
    
    return True
        

def IsBinarySearchTree(tree):
    if len(tree)>0:
        x=inOrder(tree)
        return x
    else:
        return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
