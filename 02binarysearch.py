#!/usr/bin/python
# CodeKata02 [5 Binary Chops]

list0=[]
for n in range(0,100):
	list0.append(n)
item = 3;
lb=0;
ub=len(list0)-1
#Type1[iterative]
def binarysearch0(item,lb,ub):
	while 1:
		mid=(lb+ub)/2
		if item>list0[mid]:
			lb=mid+1
		elif item<list0[mid]:
			ub=mid-1
		else:
			return list0[mid]

#Type2[Recursive]
def binarysearch1(item,lb,ub):
	mid=(lb+ub)/2
	if item>list0[mid]:
		binarysearch1(item,mid+1,ub)
	elif item<list0[mid]:
		binarysearch1(item,lb,mid-1)
	else:
		return list0[mid]

print binarysearch0(item,lb,ub)
print binarysearch1(item,lb,ub)
