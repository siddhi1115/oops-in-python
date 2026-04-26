def fact(n):
  if n < 0:
    print("Enter a positive number")
  elif n == 0:
    return 1
  else:
   return n*fact(n-1)

num = int(input("Enter a number:"))
result = fact(num)
print(f"The factorial of {num} is: {result}")