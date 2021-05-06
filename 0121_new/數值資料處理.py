import  numpy as np
#arr1 = np.arange(1,17).reshape(4,4)
#print(arr1)
#print('np_flipud')
#print(np.flipud(arr1)) #上下顛倒
#print('np_fliplr')
#print(np.fliplr(arr1)) #左右互換
#print('np_transpose')
#print(np.transpose(arr1))

print('當有多個矩陣時合併為tuple')
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11]
zip1 = zip(a,b)
print(zip1)
print(tuple(zip1))
zip2 = zip(a,c)
print(tuple(zip2))
print(list(zip(a,b))) #list中包含tuple

#使用numpy語法進行合併(形狀要相同才能合併，因此ac合併不了)
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([9,10,11])
x1 = np.stack((a,b),axis=0)
print(x1)
x2 = np.stack((a,b),axis=1)
print(x2)