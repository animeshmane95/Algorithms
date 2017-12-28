def merge(left, right):
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    i = 0
    j = 0
    sortedlist = []
    while (len(sortedlist) < len(left) + len(right)):
        if left[i] < right[j]:
            sortedlist.append(left[i])
            i += 1
        else:
            sortedlist.append(right[j])
            j += 1
        '''if i == len(left) or j == len(right):
            sortedlist.extend(left[i:] or right[j:])
            break'''
        if i == len(left):
            sortedlist.extend(right[j:])
            break
        elif j == len(right):
            sortedlist.extend(left[i:])
    return sortedlist


def mergesort(unsortedList):
    if len(unsortedList) < 2:
        return unsortedList
    middle = int(len(unsortedList) / 2)
    left = mergesort(unsortedList[:middle])
    right = mergesort(unsortedList[middle:])
    return merge(left, right)


def main():
    unsortedList = []
    lengthOfUnsortedList = int(input("Enter the length of the array"))
    for i in range(0, lengthOfUnsortedList):
        k = int(input("Enter the element:"))
        unsortedList.append(k)
    sortedList = mergesort(unsortedList)
    print(sortedList)


main()
