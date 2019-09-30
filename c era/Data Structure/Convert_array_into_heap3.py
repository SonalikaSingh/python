# python3

def isHeap(arr, n): 
    for i in range(int((n - 2) / 2) + 1):  
        if arr[2 * i + 1] > arr[i]:  
                return False
        if (2 * i + 2 < n and
            arr[2 * i + 2] > arr[i]):  
                return False
    return True

x=[]
def MaxHeapify(arr, i, n):
    y=[]
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i  
    if l < n and arr[l] < arr[i]:  
        smallest = l 
    if r < n and arr[r] < arr[smallest]:  
        smallest = r  
    if smallest != i:
        #print(arr,i,smallest)
        y.append(i)
        y.append(smallest)
        x.append(y)
        
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        MaxHeapify(arr, smallest, n)
        
    #return x
  

def convertMaxHeap(arr, n):
    result=[]
    for i in range(int((n - 2) / 2), -1, -1): 
        MaxHeapify(arr, i, n)
    return(x)



if __name__ == '__main__':
    n = int(input())
    data = [int(s) for s in input().split()]
    m=convertMaxHeap(data , n)
    print(len(m))
    for swap in m:
      print(swap[0], swap[1])
    
    
