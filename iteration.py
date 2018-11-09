mylist = ['hello','world','again']
for word in mylist:
  print(word)

print('===========')

for word in mylist:
  if word[0] == 'a':
    print(word)

print('===========')

nums = [1,2,3,4,5]

sum = 0
for num in nums:
  if num % 2 == 0:
    sum = sum + num

print(sum)