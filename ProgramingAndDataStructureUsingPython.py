
#----------------------Greatest Commom Divisior(GCD)---------------------------------------

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

#--------------------------GCD Program without using  the Storagr List-----------------------

# def gcd(m,n):
#     for i in range(1,min(m,n)+1):
#         if(m%i==0) and (n%i==0):
#             mrcf=i
#     return mrcf
# print(gcd(12,10))


#--------------------------------GCD Program with low cost-----------------------------------
# def gcd(m,n):
#     i=min(m,n)
#     while i> 0:
#         if m % i==0 and n %i==0:
#             return i
#         else:
#             i=i-1
# print(gcd(10,12))

#--------------------------------Linear Search--------------------------------------------
#
# def linearSearch(seq,v):
#     for x in seq:
#         if x==v:
#             return True
#     return False
# seq=(5,6,7,8,9,3)
# print(linearSearch(seq,9))
# #




