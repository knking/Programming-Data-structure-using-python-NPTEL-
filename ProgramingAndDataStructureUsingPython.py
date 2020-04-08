
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


#--------------------------------GCD Program with low cost-----------------------------------
def gcd(m,n):
    i=min(m,n)
    while i> 0:
        if m % i==0 and n %i==0:
            return i
        else:
            i=i-1
print(gcd(10,12))

#--------------------------------Linear Search--------------------------------------------

def linearSearch(seq,v):
    for x in seq:
        if x==v:
            return True
    return False
seq=(5,6,7,8,9,3)
print(linearSearch(seq,9))


#----------------------Binary Search------------------------
def bsearch(lst,n):
    lb=0
    ub=len(lst)-1

    while lb <= ub:
        mid=(lb+ub)//2

        if lst[mid]==n:
            return True
        else:
            if lst[mid] < n:
                lb=mid
            else:
                ub=mid

lst=[4,6,7,8,23,33,55,66,77,88]
n=23
if bsearch(lst,n):
    print("Found")
else:
    print("NOT FOUND")


#-------------Binary Search ------------

def binarySearch(lst,val,lb,ub):
    if lb-ub==0:
        return False
    mid=(lb+ub)//2

    if val==lst[mid]:
        #print("f")
        return True

    if val < lst[mid]:
        return binarySearch(lst,val,lb,mid)
    else:
        return binarySearch(lst,val,mid+1,ub)
lst=[3,4,5,6,7,9,12,13,15,17,18]

print(binarySearch(lst,13,0,len(lst)-1))

#-------------------------------Selection sort---------------------

lst=[4,6,1,8,9,21]
for start in range(len(lst)):
    minimum=start

    for i in range(start,len(lst)):
        if lst[i]<lst[minimum]:
            minimum=i
    (lst[start],lst[minimum])=(lst[minimum],lst[start])

print(lst)

#-----------------Insertion sort--------------------------------

def insertionSort(my_list):
    for index in range(1,len(my_list)):
        current_element=my_list[index]
        pos=index
        while current_element < my_list[pos-1] and pos > 0:
            my_list[pos]=my_list[pos-1]
            pos = pos-1
        my_list[pos]=current_element

num=int(input("How many element you want to insert"))
lst1=[int(input())for i in range(num)]
lst1=[3,2,5,6,7,12,13,23]
insertionSort(lst1)
print(lst1)

#---------------------Inverse function-------------------
def inverse(n):
    rev=0
    while n >0:
        (temp,n) = (n % 10,n // 10)
        rev = (rev * 10) + temp
    return rev
print(inverse(n=int(input("Enter number to reverse : "))))






