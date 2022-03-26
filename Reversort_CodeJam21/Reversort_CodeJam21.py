# Solved by Satyam Kumar
# Question link : https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
num=int(input())

# reversing the sub-list in main list
def reverse(lst,i,j):
    while i<j:

        #swapping
        t=lst[i-1]
        lst[i-1]=lst[j-1]
        lst[j-1]=t

        # adjusting the index
        i+=1
        j-=1

    return lst

# iterating over number of problems
for k  in range(0,num):
    length=int(input())  
    lst=[]
    cost=0
    
    arr=input()
    lst=arr.split(" ")
    lst=list(map(int,lst))  # list is ready
    
    # iterating over list
    for i in range(1,len(lst)):
        
        # assigning index of min value in sub-list
        j=lst.index(min(lst[i-1:len(lst)])) + 1
        lst=reverse(lst, i, j)

        #calculating the cost
        cost =cost + (j-i+1)
      

    print("Case #{}: {}".format(k+1,cost))
        
