#common element function
#define a function with two inputs return a lists
#which contains common element of both the list

#ex-->[1,3,5,7,8],[2,3,4,5]
#output [3,5]



list_1 =[1,2,3,4,5,6]
list_2 =[2,4,6]
def common_finder(n,m):
    e=[]
    for i in n:
        if i in m:
            e.append (i)
    return e
print (common_finder(list_1,list_2))
