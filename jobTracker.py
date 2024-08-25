val = input('paste the url \n')
flag = False

with open('/home/aravind/jobFile.txt', 'r') as file:
	for line in file:
		if val in line:
			flag = True
			break

if(flag == True):
	print("MATCH FOUND")
else:
	print("NOT applied")
	with open('/home/aravind/jobFile.txt', 'a') as file:
		file.write(val+'\n')
	print('added to the list')

        	# print(f"Found the string '{target_string}' in the");

# print(html_as_string.count("profile-container"))
