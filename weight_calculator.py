weight = 35
height = 4.87
#logic to calculate bmi
bmi = weight /(height ** 2)

if bmi < 18.5: # 18.5 not included
    print("underweight")
elif 18.5 <= bmi < 25 : #18.5 included but 25 not
    print("normal weight")
else:
    print("overweight")
