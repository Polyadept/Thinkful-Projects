for n in range(1,100 + 1):
  if n % 5 == 0 and n % 3 == 0:
    print("Fizzbuzz!")
  elif n % 5 == 0:
    print("Buzz!")
  elif n % 3 == 0:
    print("Fizz!")
  else:
    print(n)
    
    