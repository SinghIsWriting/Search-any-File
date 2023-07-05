#!/data/data/com.termux/files/usr/bin/python3
'''
This command is for terminal:
find $HOME -iname ab.py
'''
import os

reqf = input("Enter the file to search location: ")
a = 0
for r,d,f in os.walk("/data/data/com.termux"):
	for eachf in f:
		if eachf == reqf:
			a += 1
			print(os.path.join(r,eachf))
print()
if a == 0:
	print("File not found.")
elif a == 1:
	print(f"{a} location is found for file named {reqf}")
else:
	print(f"Total {a} locations are found for file named {reqf}")
print()
