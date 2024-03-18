
'''def common(arr,brr,m,n):
    h=[]
    for i in range(n):
        for j in range(m):
            if arr[i]==brr[j]:
                h.append(arr[i])
    
    l=len(h)
    for i in range(l):
        print(h[i],end=" ")
    
n=int(input())
m=int(input())
if n<=20 and m<=30:
    arr=[int(i) for i in input().split()]
    brr=[int(i) for i in input().split()]
    common(arr,brr,m,n)
else:
    print("enter proper size")'''


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[88,11,22,44,66,99,32,67,54,10]
l=len(arr)
bubble_sort(arr)
for i in range(l):
    print(arr[i],end=" ")


'''20
30
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30'''
