val = input('paste the url \n')
flag = False

with open('<ENTER FILE PATH>/jobFile.txt', 'r') as file:
	for line in file:
		if val in line:
			flag = True
			break

if(flag == True):
	print("MATCH FOUND")
else:
	print("NOT applied")
	with open('<ENTER FILE PATH>/jobFile.txt', 'a') as file:
		file.write(val+'\n')
	print('added to the list')

