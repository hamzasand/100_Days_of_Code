price = 0
print(" Welcome to Python Pizza Deliveries!")
size = input("whats your pizza size S,M or L?")
if size == "S":

    price = 15
        
elif size == "M":
    price = 20
else:
    price = 25

pep = input("do you want peporoni on you pizza? Y or N:")
if pep == "Y":
    if size == "S":
        price =+ 2
    else:
        price =+ 3

che = input("are you want cheez: Y or N")
if che =="Y":
    price =+1

print(f"your total bill is ${price}")