// this is the list given
p =[48, 74, 49, 35, 34,  8, 42, 29, 11, 39,
 59,  0, 46, 75, 72, 97, 77, 30, 86, 33,
 58, 24, 99, 56, 22, 38, 18, 45,  2, 23,
  4, 16, 26, 67, 79, 64,  3, 85, 55, 17,
  5, 14, 90, 20, 63, 54,  6, 89, 12, 61,
 73, 50,  7, 28, 91, 94, 81, 15, 68, 43,
 53, 36, 98, 19, 92, 76, 88, 71, 62, 41,
 93, 57, 60, 65, 21, 27, 95, 82, 52, 10,
  1, 13, 31, 44, 25, 96, 40, 66, 84, 32,
 87, 37, 83, 47, 70, 80, 69,  9, 51, 78]
//define an empty list
rlist=[]
//filling the list with recursion
def table(n):
    
    print(p[n],end=" ")
    if len(rlist) < 200:
        rlist.append(p[n])
        return table(p[n])
    return rlist
// initialize the list    
table(0)

// start here.
def iterating_over_table(N):
    ret_value = 0
    ### START YOUR CODE HERE ###
    ret_value = rlist[N-1]
    #### END YOUR CODE HERE ####
    return ret_value
