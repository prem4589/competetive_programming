import random
def rand7():
    return random.randint(1, 7)
def rand5():
    while True:
        k=rand7()
        if k< 6:
            return k
print ('Rolling 5-sided die...')
print (rand5())