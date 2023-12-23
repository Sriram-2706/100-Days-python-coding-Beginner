height = float(input())
weight = int(input())
h,w=height,float(weight)
bmi= w/h**2
if bmi<18.5:
  print("Your BMI is",bmi,", you are underweight.")
elif bmi>=18.5 and bmi<25:
  print("Your BMI is",bmi,", you have a normal weight.")
elif bmi>=25 and bmi<30:
  print("Your BMI is",bmi,", you are slightly overweight.")
elif bmi>=30 and bmi<35:
  print("Your BMI is",bmi,", you are obese.")
else:
    print("Your BMI is",bmi,", you are clinically obese.")