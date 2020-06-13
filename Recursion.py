#!/usr/bin/env python
# coding: utf-8

# # Recursion

# In[ ]:


#Recursion works on basis of PMI (Principle of mathematical induction) where we:
# task 1: prove for small no.s-BaseCase
#  task 2: assume true for k value (ASSUMPTION)- Hypothesis
#  task 3: then prove for k+1 value


# In[4]:


#######################
# Sum of no.s #
#######################

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

a=sum(int(input()))
print(a)


# In[1]:


#######################
# QN POWER OF NO.#
#######################

def power_c(x,n):
    if n==0 and x==0:
        return 1
    if n==0:
        return 1
    return x*power_c(x,n-1)


c,d=input().split(' ')

print(power_c(int(c),int(d)))


# In[2]:


########################
# Qn -PRINT FIRST N NO.S
########################

def print_n(n):
    if n==0:
        return 
    print(n)
    print_n(n-1)
    
no=int(input())
print_n(no)

    


# In[3]:


########################
# Qn Factorial Number #
########################

def fact(n):
    if n==0:
        return 1
    
    return n*fact(n-1)

no=int(input())
a=fact(no)
print(a)

#Time complexity is given by O(n)
# Recurrence relation is T(n)=T(n-1)+k
# so such operation is repeated n times until reached 0 where it returns 1


# In[7]:


########################
# Qn - Fibonacci no #
########################

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

a=fib(int(input()))
print(a)


# In[8]:


###################
# Can increase recursion limit to avoid recursion depth, but not recommended as uses lot of space #
#using sys library#

# import sys
# sys.setrecursionlimit(1000)


# In[9]:


##################
# to check if list is sorted
##################

def issorted(a):
    l=len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    
    return issorted(a[1:]) # This is a very problem because we are copying which will take a lot of space which is bad

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(issorted(arr))


# In[19]:


##################
# to check if list is sorted
##################

#Modified form 
def issorted2(a,si=0):
    l=len(a)
    if si==l or si==l-1:
        return True
    if a[si]>a[si+1]:
        return False
    return issorted2(a,si+1)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(issorted2(arr))


# In[15]:


#####################
# Qn sum of array
#####################

def sum_array(n):
    l=len(n)
    if l==1:
        return n[0]
    return n[0]+sum_array(n[1:])

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sum_array(arr))


# In[18]:


#####################
# QN check no. in array
#####################

def check_array(n,x):
    l=len(n)
    if l==0:
        return
    if n[0]==x:
        return True
    return check_array(n[1:],x)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
a=check_array(arr,x)
if a:
    print('Found x')
else:
    print('Not Found')


# In[23]:


#####################
# First occure of x in list
#####################

def firstindex(arr,x,si=0):
    l=len(arr)
    if si==l:
        return -1
    if arr[si]==x:
        return si
    return firstindex(arr,x,si+1)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
a=firstindex(arr,x)
print(a)


# In[26]:


#####################
# Last occurence of x in list
#####################

def lastindex(arr,x):
    l=len(arr)
    if l==0:
        return -1
    p=lastindex(arr[1:],x)
    if p!=-1:
        return p+1
    else:
        if arr[0]==x:
            return 0
        else:
            return -1
        
# To improve this code so that no waste is created        
def lastindex2(arr,x,si=0):
    l=len(arr)
    if si==l:
        return -1
    p=lastindex2(arr,x,si+1)
    if p!=-1:
        return p
    else:
        if arr[si]==x:
            return si
        else:
            return -1
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
a=lastindex(arr,x)
b=lastindex2(arr,x)
print(a)
print(b)


# In[37]:


####################
# Qn replace all occurence of 'character' with another 'character' in string
####################

def replacewith(s,a,b):
    l=len(s)
    if l==0:
        return s
    if s[0]==a:
        return b+s[1:]
    return s[0]+replacewith(s[1:],a,b)

def replacewith2(s,a,b):
    l=len(s)
    if l==0:
        return s
    p=replacewith(s[1:],a,b)
    if s[0]==a:
        return b+p
    else:
        return s[0]+p


replacewith('hello','o','p')
replacewith2('hello','o','p')


# In[40]:


def removechar(str,x):
    l=len(str)
    if l==0:
        return str
    p=removechar(str[1:],x)
    if str[0]==x:
        return p
    else:
        return str[0]+p

string = input()
d=input()
print(removechar(string,d))


# In[49]:


#######################
#QN replce pi with 3.14
#######################
def replacepi(stri):
    l=len(stri)
    # need to check if 2 characters simuntaneously is pi
    if l==0 or l==1:
        return stri
    if stri[0]=='p' and stri[1]=='i':
        return str(3.14)+replacepi(stri[2:])
    else:
        return stri[0]+replacepi(stri[1:])
    
s=input()
replacepi(s)


# In[51]:


#####################
# qn remove consecutive duplicates from a string
#####################

def removedup(s):
    l=len(s)
    if l==0 or l==1:
        return s
    
    if s[0]==s[1]:
        return removedup(s[1:])
    else:
        return s[0]+removedup(s[1:])

s=input()
removedup(s)

        
    
    


# In[55]:


####################
#Binary search for array (Only for sorted)
####################

def binarysearch(arr,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if arr[mid]==x:
        return mid
    if arr[mid]>x:
        return binarysearch(arr,x,si,ei=mid-1)
    else:
        return binarysearch(arr,x,mid+1,ei)
    

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
binarysearch(arr,x,0,n-1)


# In[58]:


#######################
#Qn Merge Sort
# In merge sort we divide 2 arrays  and sort these two seperately and then merge these 2 sorted arrays
#######################

def merge(a,b,arr):
    i=0
    j=0
    k=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            arr[k]=a[i]
            i+=1
            k+=1
        else:
            arr[k]=b[j]
            k+=1
            j+=1
    
    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    
    while j<len(b):
        arr[k]=b[j]
        k+=1
        j+=1
            
def mergesort(arr):
    l=len(arr)
    if l==0 or l==1:
        return 
    mid=l//2
    
    a=arr[0:mid]
    b=arr[mid:]
    
    mergesort(a)
    mergesort(b)
    
    merge(a,b,arr)
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergesort(arr)
print(arr)
    


# In[61]:


###################
# Qn Quick Sort
#Lets pich any elemrnt andd make it reach its right place- this can be done by  coutning no. of elements
# smaller than it,that will be its correct position
# Move all smaller no.s towards left and all larger no. towards right
#and then partition in 2 list and sort thee left part and right part
# Its diff from merge sort because in that we directly call merge sort on two halves and then sort
# In quick sort does work first and then calls also no copies have to be made !!!
##################

def partition(arr,si,ei):
    pivot=arr[si]
    count=0
    for i in range(si,ei+1):
        if pivot>arr[i]:
            count+=1
    
    arr[si],arr[count+si]=arr[count+si],arr[si]
    pivot_index=count+si
    
    i=si
    j=ei
    while i<j:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>pivot:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
            
    return pivot_index

def quicksort(arr,start,end):
    if start>=end:
        return
    
    p=partition(arr,start,end)
    quicksort(arr,start,p-1)
    quicksort(arr,p+1,end)
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quicksort(arr,0,n-1)
print(arr)
    


# In[71]:


#####################
# Qn Tower of Hanoi #
# Only 1 disk at a time and smaller disk on larger only
# Print all the steps you will take
#####################

def Hanoi(n,source,helper,target):
    if n==0:
        return 
    Hanoi(n-1,source,target,helper)
    print(source,'-->',target)
    Hanoi(n-1,helper,source,target)

Hanoi(4,'a','b','c')
        


# In[80]:


########################
# Qn Sum of digits of a number #
########################

def sum_of_digits(n):
    l=len(n)
    if l==0:
        return 0
    
    return int(n[0])+sum_of_digits(n[1:])

d=input()
print(sum_of_digits(d))


# In[83]:


########################
# Qn check if Palindrome or  not
########################

def palin(s):
    l=len(s)
    if l==1 or l==0:
        return True
    
    return s[0]==s[-1] and palin(s[1:l-1])

c=input()
a=palin(c)
if a:
    print('Palindrome')
else:
    print('Not a Palindrome')


# In[91]:


#######################
# Qn geometric sum
#######################

def geometric_s(c):
    if c==0:
        return 1
    return 1/(2**c)+geometric_s(c-1)

c=int(input())
print('{:.5f}'.format(geometric_s(c)))


# In[93]:


########################
# Qn multiplication recursive
########################

def mult(m,n):
    if n==0 or m==0:
        return 0
    if m==1:
        return n
    
    return m+mult(m,n-1)

c=int(input())
d=int(input())
print(mult(c,d))


# In[97]:


######################
# count no. of zeroes in integer
######################

def  count_0(n):
    if n==0:
        return 0
    if n%10==0:
        return 1+count_0(n//10)
    else:
        return count_0(n//10)
    
c=int(input())
print(count_0(c))


# In[101]:


print(ord('1'))


# In[107]:


#########################
# Qn convert string to integer
#########################


def convert(s):
    l=len(s)
    if l==1:
        return (ord(s)-ord('0'))
    
    x=ord(s[0])-ord('0')
    return x*(10**(l-1))+convert(s[1:])

print(convert(input()))
    


# In[112]:


###########################
# Qn Pair star - input-hello,output-hel*l0
###########################

def pairstar(s):
    l=len(s)
    if l==0 or l==1:
        return s
    
    if s[0]==s[1]:
        return s[0]+'*'+pairstar(s[1:])
    else:
        return s[0]+pairstar(s[1:])

d=input()
print(pairstar(d))


# In[115]:


##################################
# CHECK AB
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
###################################

def checkab(s,si=0):
    l=len(s)
    if s[0]=='a':
        if si==l-1:
            return True
        if s[si]=='a':
            if s[si+1]=='a':
                return checkab(s,si=si+1)
            elif s[si+1]=='b' and s[si+2]=='b':
                return checkab(s,si=si+2)
            else:
                return False
        
        if s[si]=='b':
            if s[si+1]=='a':
                return checkab(s,si=si+1)
            else:
                return False
            
    
d=input()
print(checkab(d))
        


# In[131]:


#########################
# Qn staircase
# Can hop 1,2,3 stairs at a time 
# Find no. of ways to do it
#########################

def staircase(n):
    if n==0:
        return 1
    
    if n<0:
        return 0
    
    if n==2:
        return 2
    if n==3:
        return 4
    
    x=staircase(n-1)
    y=staircase(n-2)
    z=staircase(n-3)
    
    return x+y+z

c=int(input())
print(staircase(c))


# In[ ]:




