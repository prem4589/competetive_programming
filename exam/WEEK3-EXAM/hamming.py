def to_binary(a):
	l=[]
	while(a>0):
		d=a%2
		l.append(d)
		a=a//2
	return l[::-1]

def check(n,m):
	l1=[]
	l2=[]
	x=to_binary(n)
	y=to_binary(m)
	lenx=len(x)
	leny=len(y)
	lenl1=8-len(x)
	lenl2=8-len(y)
	for i in range(lenl1):
		l1.append(0)
	l1.extend(x)
	for i in range(lenl2):
		l2.append(0)
	l2.extend(y)

	count=0
	for i in range(len(l1)):
		for j in range(len(l2)):
			if l1[i]!=l2[j]:
				count+=1
				break
			else:
				break
	print(count)


check(1,4)
check(25,30)
check(100,250)
check(1,30)
check(0,255)