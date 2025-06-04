r=7
unit=2
n=8
arr=[2,8,3,5,7,4,1,2]
food_required=r*unit
if(len(arr)==0):
    print(-1)

for i in range(n):
    food_required=food_required-arr[i]
    if(food_required<0):
        break
if(food_required>0):
    print(0)
print(abs(food_required))