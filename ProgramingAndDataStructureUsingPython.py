
#----------------------Greatest Commom Divisior(GCD)---------------------------------------

def gcd(m,n):
    factM=[]
    for i in range(1,m+1):
        if m %i==0:
            factM.append(i)
    factN=[]
    for j in range(1,n+1):
        if n % j ==0:
            factN.append(j)
    finalFact=[]
    for k in factM:
        if k in factN:
            finalFact.append(k)
    return finalFact[-1]
print(gcd(22,20))

#--------------------------GCD Program without using  the Storagr List-----------------------

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if(m%i==0) and (n%i==0):
            mrcf=i
    return mrcf
print(gcd(12,10))




