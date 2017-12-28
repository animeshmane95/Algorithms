def binarySearch(array,start,end,value):
    while(start<=end):
        guess = int((start+end)/2);
        if(array[guess] == int(value)):
            return  guess
        elif (array[guess]< value):
            start = guess + 1;
            binarySearch(array,start,end,value)
        else:
            end = guess - 1;
            binarySearch(array,start,end,value)

    return -1

array = [20,30,40,50,60,70,80]
end = len(array) - 1
start = 0
value = int(input("Enter the value you want to search"))
guess = binarySearch(array,start,end,value)
print("The value %d is at postion : %d"%(value,guess))