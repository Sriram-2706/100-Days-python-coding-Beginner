import math

def pcalc(h,w,c):
  n=math.ceil(h*w/c)
  print(f"You'll need {n} cans of paint.")

h = int(input()) 
w = int(input()) 
c = 5
pcalc(h,w,c)
