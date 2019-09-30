# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    temp=[]
    i=0;j=0
    temp.append(i)
    flag=0
    
    while(flag==0):
      if(self.left[j] != (-1)):
        temp.append(self.left[j])
        j=self.left[j]
      else:
        if len(temp) != 0:
          x=temp.pop()
          self.result.append(self.key[x])
          if(self.right[x] != (-1)):
            temp.append(self.right[x])
            j=self.right[x]
        else:
            flag=1
      #print(temp)
    return self.result
            
     
  def preOrder(self):
    self.result = []
    temp=[]
    i=0;j=0
    temp.append(i)
    flag=0

    while(flag == 0):
      x=temp.pop()
      self.result.append(self.key[x])
      if(self.right[x] != (-1)):
            temp.append(self.right[x])
      if(self.left[x] != (-1)):
        temp.append(self.left[x])
      if len(temp) == 0:
        flag=1
      #print(temp)
      
    return self.result

  def postOrder(self):
    self.result = []
    temp=[]
    i=0;j=0
    temp.append(i)
    flag=0
    x="a"
    while(flag==0):
      if(self.left[j] != (-1)):
        temp.append(self.left[j])
        j=self.left[j]
      else:
        top=temp[len(temp)-1]
        if self.right[top] != x and(self.right[top] != (-1)):
            temp.append(self.right[top])
            j=self.right[top]
        else:
          x=temp.pop()
          self.result.append(self.key[x])
        if len(self.result) == self.n:
          flag=1
        
      #print(temp)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
