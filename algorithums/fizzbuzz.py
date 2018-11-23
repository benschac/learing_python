def fizz_buzz(num):
  """
  Takes number as input and prints
  fizz if number is % 3
  buzz if number is % 5
  fizzbuzz if number is % 3 and % 5 
  """
  for x in range(1, num + 1):
    if x % 3 == 0 and x % 5 == 0:
      print('fizzbuzz')
    elif x % 5 == 0:
      print('buzz')
    elif x % 3 == 0:
      print('fizz')
    else:
      print(x)

fizz_buzz(45);