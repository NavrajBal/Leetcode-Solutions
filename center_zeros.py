# The problem is given an array of integers return an array
# with all zeros centered in the middle of the array and the other integers 
# to the left and right while maintaining their original order


def center_zeros(arr):

    length = len(arr)
    newlist = []


    #find number of zeros in the array
    zc = 0

    for i in range(length):
        if arr[i]:
            zc += 1

    #determine number of elements on each side
    nze = length - zc
    leftsize = nze // 2


    #create new array
    for i in range(length):
        if (len(newlist) == leftsize):
            for j in range(zc):
                newlist.append(0)
        elif arr[i] != 0:
            newlist.append(arr[i])

    
    return newlist

        
#Tests
assert center_zeros([0, 1, 2, 3, 4])



