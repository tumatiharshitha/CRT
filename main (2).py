# Enter your code here
def quick_sort(arr):

    if len(arr)<=1:
        return arr
    
    left=[]
    right=[]
    equal=[]
    povt=arr[-1]

    for i in arr:
        if(i<povt):
            left.append(i)
        elif(i>povt):
            right.append(i)
        else:
            equal.append(i)
        print("pivot:",povt)
        print("left sub array",left)
        print("right sub array",right)
        print("equal array",equal)
        return quick_sort(left)+equal+quick_sort(right)

arr = [23,63,44,57,12,45,36]
sorted_arr=quick_sort(arr)
print(sorted_arr)
