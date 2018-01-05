def maximum_cross_subarray(array, low, mid, high):
    leftsum = float('-inf')
    print(leftsum)
    sum1 = 0
    maxleft = 0
    maxright = 0
    for i in range(low, mid):
        sum1 = sum1 + array[i]
        if sum1 > leftsum:
            leftsum = sum1
            maxleft = i
    rightsum = float('-inf')
    sum2 = 0
    for j in range(mid + 1, high):
        sum2 = sum2 + array[j]
        if sum2 > rightsum:
            rightsum = sum2
            maxright = j
    return maxleft, maxright, leftsum + rightsum


def maximumsubarray(array, low, high):
    if low == high:
        return low, high, array[low]
    else:
        mid = int((low + high) / 2)
        (leftlow, lefthigh, leftsum) = maximumsubarray(array, low, mid)
        (rightlow, righthigh, rightsum) = maximumsubarray(array, mid + 1, high)
        (lowcross, highcross, crosssum) = maximum_cross_subarray(array, low, mid, high)
    if leftsum > rightsum and leftsum > crosssum:
        return leftlow, lefthigh, leftsum
    elif rightsum > leftsum and rightsum > crosssum:
        return rightlow, righthigh, rightsum
    else:
        return lowcross, highcross, crosssum


def main():
    array = []
    maximumSubarray = []
    length_of_array = int(input("Enter the number of elements you want to enter in the array"))
    for i in range(0, length_of_array):
        k = int(input("Enter the element at position %d:" % i))
        array.append(k)
    print("The entered array is")
    print(array)
    (maxsubarraylow, maxsubarrayhigh, maxsum) = maximumsubarray(array, 0, length_of_array -1)
    print(maxsubarrayhigh)
    print(maxsubarraylow)
    for i in range(maxsubarraylow, maxsubarrayhigh):
        maximumSubarray.append(array[i])
    print(maximumSubarray)
    print(maxsum)
main()
