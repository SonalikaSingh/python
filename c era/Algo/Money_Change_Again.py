# Uses python3
import sys

def check(m,p):
    count=0
    l=[]
    while(m>=p):
        m=m-p
        count+=1
    l.append(m)
    l.append(count)
    return l

def get_change(m):
    count=0
    x=check(m,4)
    
    if x[0]<3 and m>=4:
        y=check(x[0],1)
        z=check(x[0]+4,3)
        
        if y[1]<z[1]:
            count+=x[1]+y[1]
        else:
            count+=x[1]+z[1]-1
    else:
        l1=check(x[0],3)
        count+=l1[1]+l1[0]
        
            
        
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

