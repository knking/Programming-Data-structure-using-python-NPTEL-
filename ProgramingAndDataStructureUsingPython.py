#
# #----------------------Greatest Commom Divisior(GCD)---------------------------------------
#
# def gcd(m,n):
#     factM=[]
#     for i in range(1,m+1):
#         if m %i==0:
#             factM.append(i)
#     factN=[]
#     for j in range(1,n+1):
#         if n % j ==0:
#             factN.append(j)
#     finalFact=[]
#     for k in factM:
#         if k in factN:
#             finalFact.append(k)
#     return finalFact[-1]
# print(gcd(22,20))
#
# #--------------------------GCD Program without using  the Storagr List-----------------------
#
# def gcd(m,n):
#     for i in range(1,min(m,n)+1):
#         if(m%i==0) and (n%i==0):
#             mrcf=i
#     return mrcf
# print(gcd(12,10))
#
#
# #--------------------------------GCD Program with low cost-----------------------------------
# def gcd(m,n):
#     i=min(m,n)
#     while i> 0:
#         if m % i==0 and n %i==0:
#             return i
#         else:
#             i=i-1
# print(gcd(10,12))
#
# #----------------------------Array in Python-----------------
#
# import array
# arr=array.array('i',[3,4,5,6,3,7])
# print("Old array : " )
# for i in range(0,len(arr)):
#     print(arr[i],end=" ")
# arr.append(10)
# print('\r')
# print("New array : ")
# for j in range(0,len(arr)):
#     print(arr[j],end=" ")
# print('\r')
# print(arr.index(10))
# arr.reverse()
# print("After reverse the vale of array is : ")
# for j in range(0,7):
#     print(arr[j],end=" ")
#
#
# #--------------------------------Linear Search--------------------------------------------
#
# def linearSearch(seq,v):
#     for x in seq:
#         if x==v:
#             return True
#     return False
# seq=(5,6,7,8,9,3)
# print(linearSearch(seq,9))
#
#
# #----------------------Binary Search------------------------
# def bsearch(lst,n):
#     lb=0
#     ub=len(lst)-1
#
#     while lb <= ub:
#         mid=(lb+ub)//2
#
#         if lst[mid]==n:
#             return True
#         else:
#             if lst[mid] < n:
#                 lb=mid
#             else:
#                 ub=mid
#
# lst=[4,6,7,8,23,33,55,66,77,88]
# n=23
# if bsearch(lst,n):
#     print("Found")
# else:
#     print("NOT FOUND")
#
#
# #-------------Binary Search ------------
#
# def binarySearch(lst,val,lb,ub):
#     if lb-ub==0:
#         return False
#     mid=(lb+ub)//2
#
#     if val==lst[mid]:
#         #print("f")
#         return True
#
#     if val < lst[mid]:
#         return binarySearch(lst,val,lb,mid)
#     else:
#         return binarySearch(lst,val,mid+1,ub)
# lst=[3,4,5,6,7,9,12,13,15,17,18]
#
# print(binarySearch(lst,13,0,len(lst)-1))
#
# #-------------------------------Selection sort---------------------
#
# lst=[4,6,1,8,9,21]
# for start in range(len(lst)):
#     minimum=start
#
#     for i in range(start,len(lst)):
#         if lst[i]<lst[minimum]:
#             minimum=i
#     (lst[start],lst[minimum])=(lst[minimum],lst[start])
#
# print(lst)
#
# #-----------------Insertion sort--------------------------------
#
# def insertionSort(my_list):
#     for index in range(1,len(my_list)):
#         current_element=my_list[index]
#         pos=index
#         while current_element < my_list[pos-1] and pos > 0:
#             my_list[pos]=my_list[pos-1]
#             pos = pos-1
#         my_list[pos]=current_element
#
# num=int(input("How many element you want to insert"))
# lst1=[int(input())for i in range(num)]
# lst1=[3,2,5,6,7,12,13,23]
# insertionSort(lst1)
# print(lst1)
#
# #---------------------Inverse function-------------------
# def inverse(n):
#     rev=0
#     while n >0:
#         (temp,n) = (n % 10,n // 10)
#         rev = (rev * 10) + temp
#     return rev
# print(inverse(n=int(input("Enter number to reverse : "))))
#
#
#
# def anangram_str(str1, str2):
#     sort_str1=sorted(str1)
#     sort_str2=sorted(str2)
#     if len(str1)==len(str2):
#         if sort_str1==sort_str2:
#             print("Given string is   Anagram")
#         else:
#             print("Given String is not  Anagram")
# # s1="earth"
# # s2="heart"
# anangram_str("earth","heart")
#

#--------------------------Quick sort-----------------------------------------

def quicksort(A,l,r):
    if r-l<=1:
        return 0
    yellow=l+1

    for green in range(l+1,r):

        if A[green]<=A[l]:
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow=yellow+1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])

    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)

l=list(range(5,0,-1))
#print(l)
quicksort(l,0,len(l))
print(l)