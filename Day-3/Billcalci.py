print("Thank you for choosing Python Pizza Deliveries!")
s = input() 
a = input()
e = input() 
t=0
if s=='S':
  t+=15
  if a=='Y':
    t+=2
  else:
    pass
  if e=='Y':
    t+=1
  else:
    pass
  print(f"Your final bill is: ${t}.")
elif s=='M':
  t+=20
  if a=='Y':
    t+=3
  else:
    pass
  if e=='Y':
    t+=1
  else:
    pass
  print(f"Your final bill is: ${t}.")
else:
    t+=25
    if a=='Y':
      t+=3
    else:
      pass
    if e=='Y':
      t+=1
    else:
      pass
    print(f"Your final bill is: ${t}.")

