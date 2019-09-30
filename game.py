def minimumPasses(m, w, p, n):
    total=0
    left=0
    count=0
    left1=0
    while(left<=n):
        candies=m*w
        left+=candies+left1
        buy=candies//p
        print(buy)
        w=w+buy
        """for i in range(buy):
            if(i%2==0):
                w=w+1
            else:
                m=m+1"""
        count+=1
        left1=candies%p
    return count
