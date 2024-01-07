sh = input().split()
k=0
m=0
for n in range(0, len(sh)):
  sh[n] = int(sh[n])
  k+=sh[n]
  m+=1

print("total height =",k)
print("number of students =",m)
print("average height =",int(round((k/m),0)))

