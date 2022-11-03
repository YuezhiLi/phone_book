import random

total = random.randint(50, 2000)
file = open('tests/test3', 'a')
file.write(str(total) + "\n")
for _ in range(total):
  length = random.randint(4, 20)
  phone_no = ''
  for _ in range(length):
    phone_no += str(random.randint(0, 10))
  query = "add " + phone_no + " name\n"
  file.write(query)

file.close();
