# Set comprehension
unique_even_sqr = {i**i for i in range(1,10) if i%2==0}
print(unique_even_sqr)