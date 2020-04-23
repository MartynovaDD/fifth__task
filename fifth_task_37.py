import os
name_of_file = 'data.txt'


def Sequence(filename):
    sum = 0
    n=0
    res = 0
    Z = 0
    ans = 0
    try:
        f=open(filename, "r")
        for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']: 
            try:
                sum+=int(s)
                n+=1
            except:
                print('word ',s,' ignored',sep='')
        if (n>0):
            res = sum/n
        elif (n==0):
            return ArithmeticError
        f.close()
        f=open(filename, "r")
        for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']: 
            try:
                Z = Z +((int(s)-res)**2)
            except:
                print('word ',s,' ignored',sep='')
        ans = Z/n
        f.close()
        return ans
    except FileNotError:
        return None

average = Sequence(name_of_file)

if (average == None):
    print("Can't open file")
elif (average == ArithmeticError):
    print("Empty file")
else:
    print("average =",average)

    





