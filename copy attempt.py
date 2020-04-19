set1 = {'apple'}

item = 'apple'
iterator = 1

while item + str(iterator) in set1:
	iterator += 1

item = item + str(iterator)
	
set1.add(item)

print(set1)
