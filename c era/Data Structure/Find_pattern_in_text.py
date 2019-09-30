# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pat, txt):
    d=256
    q=13
    
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0
    p = 0    
    t = 0    
    h = 1
    result=[]
    
    for i in range(M-1): 
        h = (h * d)% q  
    for i in range(M): 
        p = (d * p + ord(pat[i]))% q 
        t = (d * t + ord(txt[i]))% q 
  
    for i in range(N-M + 1): 
        if p == t: 
            if txt[i:i+M]==pat:
                result.append(str(i))
  
  
        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q 
  
            if t < 0: 
                t = t + q 
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

