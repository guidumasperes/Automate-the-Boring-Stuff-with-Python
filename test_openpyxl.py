import os, pyexcel_ods

files = os.listdir("C:\\Users\\Gui\\Desktop\\MyPythonScripts\\ods_files")
total = 0
for file in files:
	data = pyexcel_ods.get_data("C:\\Users\\Gui\\Desktop\\MyPythonScripts\\ods_files\\" + file)
	key = data.keys()
	key = list(key)
	sheet = data[key[0]]
	sheet = sheet[1:]
	fileTotal = 0
	for line in sheet:
		if line:
			fileTotal += float(line[4])
	print("Total in " + str(file) + " is " + str(fileTotal))
	total += fileTotal
print("Total amount is: " + str(total))