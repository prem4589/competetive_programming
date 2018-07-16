import random
def rand5():
    return random.randint(1, 5)
def rand7():
    m=5*(rand5()-1)
    n=rand5()
    res=m+n
    if res<= 21:
        return res%7+1
print ('Rolling 7-sided die...')
print (rand7())