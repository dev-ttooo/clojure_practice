num = int(input('enter some integer :'))

def prime_judge():
  for p in range(2,num):
    if num % p == 0:
      print('this is composite')
      break
  print('this is PRIME')

prime_judge()
