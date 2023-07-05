import os   # importing os module to deal with directories and files

path = input("Main directory/drive path: ")
requiredFile = input("Enter the file to search location: ")

count= 0
# walking through this path and all the directorries in this path to search the required file
for r,d,files in os.walk(path):
	for file in files:
		# when file is present in the list of files of current directory
		if file == requiredFile:
			count+= 1
			print(os.path.join(r,file))  # full path of the file
print()
if count== 0:
	print("File not found.")
elif count== 1:
	print(f"{count} location is found for file named {requiredFile}")
else:
	print(f"Total {count} locations are found for file named {requiredFile}")
print()
