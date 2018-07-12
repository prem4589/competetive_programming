def check(l,d):
	l1=[]
	for i in l:
		temp=''
		count=0
		for j in i:
			temp+=d[j]
		# print(temp)
		l1.append(temp)
		temp=''
	l2=[]
	for i in l1:
		if i not in l2:
			l2.append(i)
	print(len(l2))

d={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'}
check(["gin","zen","gig","msg"],d)
check(["a","z","g","m"],d)
check(["bhi","vsv","sgh","vbi"],d)
check(["a","b","c","d"],d)
check(["hig","sip","pot"],d)