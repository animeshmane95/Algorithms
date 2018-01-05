def peak_finder(peak_array,low,high,n):
    mid = int (low + (high - low)/2)

    if((mid == 0 or peak_array[mid - 1]<=peak_array[mid])
       and (mid == n-1 or peak_array[mid+1] <= peak_array[mid])):
        return peak_array[mid]
    elif (mid > 0 and peak_array[mid-1] > peak_array[mid]):
        return peak_finder(peak_array, low, (mid -1), n)
    else :
        return peak_finder(peak_array,mid+1,high,n)

peak_array =[]
array_size = 1
while array_size == 1 :
    element = int(input("Enter the element of the array"))
    peak_array.append(element)
    continue_array = input("Do you wish to continue?(Y/N)")
    if continue_array == "N":
        break
print("The enterd array is:")
print(peak_array)
n = len(peak_array)
peak = int(peak_finder(peak_array,0,len(peak_array) - 1,n))
print("Peak : %d" %peak)