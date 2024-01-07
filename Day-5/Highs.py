# Input a list of student scores
ss = input().split()
m=0
for n in range(0, len(ss)):
  ss[n] = int(ss[n])
  m+=1
for i in range(0,m):
  for j in range(i+1,m):
    if ss[i]>ss[i+1]:
      ss[i],ss[j]=ss[j],ss[i]

x=ss[-1]
print("The highest score in the class is:",x)