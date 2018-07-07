def anagra(s1,s2):
    s5='';s6=''
    s3=s1.lower()
    s4=s2.lower()
    for i in s3:
        if i==' ':
            continue
        else:
            s5+=i
    for i in s4:
        if i==' ':
            continue
        else:
            s6+=i
    cop = list(s6)
    pos1 = 0
    fine = True
    while pos1 < len(s5) and fine:
        pos2 = 0
        found = False
        while pos2 < len(cop) and not found:
            if s5[pos1] == cop[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            cop[pos2] = None
        else:
            fine = False

        pos1 = pos1 + 1
    return fine
str1=input()
str2=input()
print(anagra(str1,str2))