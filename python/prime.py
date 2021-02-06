num = int(input('enter some integer :'))

def prime_judge():
  for p in range(2,num):
    if num % p == 0:
      print('素数ではありません')
      break
    print(p)

prime_judge()
