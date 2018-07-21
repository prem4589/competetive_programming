def check2(n,l2):
	count=0
	l=[]
	while n>0:
		d=n%2
		n=n//2
		l.append(d)
		l=l[::-1]
	for i in l:
		if i==1:
			count+=1
	l2.append(count)
	return l2
def check(n):
	l=[]
	for i in range(n+1):
		x=check2(i,l)
	print(x)
check(15)
check(16)
check(1)
check(25)
check(5)
check(6)