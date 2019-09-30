#python3
import sys
l=[]
a=[]
def Push(n):
    l.append(n)
    if len(a)==0 or n>=a[len(a)-1] :
        a.append(n)
    
def Pop():
    x=l.pop()
    if x==a[len(a)-1]:
        a.pop()
def maximum(l):
    return max(l)



if __name__ == '__main__':

    num_queries = int(sys.stdin.readline())
    m=[]
    for i in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            Push(int(query[1]))
        elif query[0] == "pop":
            Pop()
        elif query[0] == "max" :
            
            print(a[len(a)-1])
        
        else:
            assert(0)
    
    
    
    
    
    
