#!/usr/bin/python

# CodeKata02.01 [5 Binary Chops]

list0=[]
for n in range(0,100):
	list0.append(n)
item = 3;
lb=0;
ub=len(list0)-1
mid=(lb+ub)/2
def binarysearch0(item,lb,ub):
	while 1:
		mid=(lb+ub)/2
		if item>list0[mid]:
			lb=mid+1
		elif item<list0[mid]:
			ub=mid-1
		else:
			return list0[mid]
		if lb>ub:
			return "Not Found!"

print binarysearch0(item,lb,ub)
