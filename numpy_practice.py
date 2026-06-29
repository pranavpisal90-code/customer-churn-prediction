import numpy as np

arr=np.array([1,2,3,4,5])

print(arr)

arr1=np.array([7,8,9,10])

print(arr1[0:4])

arrre=np.concatenate((arr,arr1))
print(arrre)


x=np.array_split(arrre,3)
print(x)


y=np.where((arrre==3))
print(y)


print(np.sort(arr1))

