'''L=[]
n=int(input("How many elements you want to enter:"))
print("Enter elements in a list\n")
for i in range(1,n+1):
  print("Enter element:",end=' ')
  x=int(input())
  L.append(x)
while True:
  ch=int(input("Enter 1 to show all the elements in a list\n Enter 2 to show specific elements of list\n Enter 3 to print size of list\n Enter 4 to add an element in a list\n Enter 5 to delete an element from list\n Enter 6 to delete an element from a specific position\n Enter 7 to add an element to a specific position\n Enter 8 to print all elements of list in ascending order\n Enter 9 to print all elements in descending order\n Enter 10 to print all elements in reverse\n Enter 11 to exit\n Enter 12 to continue loop:"))
  if ch==1:
    for i in L:
      print(L,end="\t")
  elif ch==2:
    x=int(input("Enter an element to be shown:"))
    a=L.index(x)
    print("\nThe element is at position:",a+1)
  elif ch==3:
    a=len(L)
    print("\nThe size of list:",a)
  elif ch==4:
    x=input("\nEnter the element to be added:")
    L.append(x)
    print("\n The new list:",L)
  elif ch==5:
    x=input("\nEnter the element to be deleted:")
    for i in L:
      L.remove(x)
    print("\nThe resulted list:",L)
  elif ch==6:
    x=input("\nEnter the element to be deleted:")
    y=int(input("\nMention the position:"))
    L.pop(x,y-1)
    print("\nThe resulted list:",L)
  elif ch==7:
    x=input("\nEnter the element to be added:")
    y=int(input("\nMention the position:"))
    L.insert(x,y-1)
    print("\nThe resulted list:",L)
  elif ch==8:
    x=L.sort()
    for i in L:
      print(i,end="\t")
  elif ch==9:
    x=L.sort(reverse=True)
    for i in L:
      print(i,end="\t")
  elif ch==10:
    L.reverse()
    print("\n The reverse list:",L)
  elif ch==1:
    print("\nPROGRAM COMPLETED SUCCESSFULLY!!!")
  else:
    print("\nInvalid Choice.")'''
#WAP that takes two lists L and M of the same size and adds their elements together to form a new list N whose N whose elements are sums of the corresponding elements in L and M.
'''L1=[]
L2=[]
n=int(input("How many elements you want to enter:"))
print("Enter elements in a list 1\n")
for i in range(n):
  print("Enter element:",end=' ')
  x=int(input())
  L1.append(x)
print("Enter elements in a list 2\n")
for i in range(n):
  print("Enter element:",end=' ')
  x=int(input())
  L2.append(x)
N=[]
for i in range(n):
  N.append(L1[i]+L2[i])
print("\nThe resulted list:",N)'''
#WAP that rotates the elements of a list so that the element at the first index,moves to the second index,the element in the second index moves to the third index etc. and the element in the last index moves to the first index
n=int(input("Enter the number of elements in the specified list:"))
L=[]
for i in range(n):
  x=input("Enter the element to be added:")
  L.append(x)
print("The original list:",L)
L[1],L[2],L[3],L[n]=p,q,r



  

    