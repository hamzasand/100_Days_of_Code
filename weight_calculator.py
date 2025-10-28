weight = 35
height = 1.87

bmi = weight /(height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25 :
    print("normal weight")
else:
    print("overweight")