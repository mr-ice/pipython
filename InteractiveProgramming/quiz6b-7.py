
n = 1000

numbers = range(2,n)

results = list()

while len(numbers) > 0:
    this = numbers[0]
    results.append(this)
    numbers = [ item for item in numbers if item % this != 0 ] 

print len(results)
