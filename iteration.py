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

print('===========')

word = 'hello'

for char in word:
  print(char)

print('===========')

mytuples = [(1,1,3),(1,2,2),(1,3,1)]

for item in mytuples:
  print item

for a,b,c in mytuples:
  print b

print('=========== iterates through keys fo doc by default')

doc = {
  'one': 1,
  'two': 2,
  'three': 3
}

for item in doc:
  print item

print('=========== but you can grab the items like so...')

for item in doc.items():
  print(item)

for key,value in doc.items():
  print(value)