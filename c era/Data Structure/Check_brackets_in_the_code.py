# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    flag=0
    for i, next in enumerate(text):
        l=[]
        if next in "([{":
            l.append(next)
            l.append(i+1)
            opening_brackets_stack.append(l)
            flag=1
           


        if next in ")]}":
            #print(opening_brackets_stack) 
            l.append(next)
            l.append(i+1)
            opening_brackets_stack.append(l)
            if flag==0:
                return i+1
            
            if len(opening_brackets_stack)>1:
                right=opening_brackets_stack.pop()
                left=opening_brackets_stack.pop()
                if are_matching(left[0], right[0]):
                    pass
                else:
                    return i+1
            
    #print(opening_brackets_stack)        

    if len(opening_brackets_stack)==0:   
        return "Success"
    else:
        return opening_brackets_stack[0][1]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

