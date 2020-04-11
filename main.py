#l=[4,1,3,1,2,3,4]
l=[]
p=input("Enter number of elements you want to store in a list ")
p=int(p)
for i in range(p):
  q=input("Enter element at ")
  l.append(q)
#p=len(l)
for i in range(p):
  n=l.count(l[i])
  if n<2:
    print(l[i])
